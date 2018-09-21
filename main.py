from operation_expression.exp_tree_to_mid_exp import exp_tree_to_mid_exp
from operation_expression.mid_expression_to_post_expresiion import mid_expression_to_post_expression
from operation_expression.post_expression_to_bitree import post_expression_to_bitree
from operation_expression.post_expression_to_bitree import to_reg_exp_tree
from operation_expression.generate_mid_exp import generate_mid_exp

import sys
import os
import re


"""
求两个数的最大公约数
parameters:
    x(int)：一个整数
    y(int)：另一个整数
return:
    两个整数的最大公约数
"""
def gcd(x, y):
    while y:
        t = x % y
        x = y
        y = t
    return x

"""
生成n个满足要求的四则运算表达式
parameters:
    n(int)：表达式的个数
    r(int)：参与运算的操作数的上界
结果生成两个文件，保存题目和答案
"""
def generate_expressions(n, r):
    mid_exps = []       # 生成的表达式
    answers = []        # 表达式对应的答案
    reg_mid_exps = []   # 规范化后的表达式
    exp_num = 0
    while exp_num != n:
        origin_exp = generate_mid_exp(r)                # 随机生成表达式
        mid_exp = origin_exp[:]
        post_exp = mid_expression_to_post_expression(mid_exp) # 生成后缀表达式
        exp_tree = post_expression_to_bitree(post_exp)  # 生成后缀表达式对应的二叉树
        (answer,_,_) = to_reg_exp_tree(exp_tree)        # 规范化生成的二叉树
        if not answer: # 生成的表达式出现负数，舍弃
            continue

        reg_mid_exp = exp_tree_to_mid_exp(exp_tree)     # 生成规范化后的中缀表达式
        if reg_mid_exp not in reg_mid_exps:            # 判断生成的表达式是否重复
            mid_exps.append(origin_exp)
            # 将表达式的值标准化
            common_div = gcd(answer[0], answer[1])  # 最大公约数
            answer = (int(answer[0] / common_div), int(answer[1] / common_div))  # 约分
            if answer[1] == 1:
                answer = answer[0]
            elif answer[0] > answer[1]:
                a = int(answer[0] / answer[1])
                b = answer[0] - answer[1] * a
                if b == 0:
                    answer = a
                else:
                    answer = '{:d}`{:d}/{:d}'.format(a, b, answer[1])
            else:
                answer = '{:d}/{:d}'.format(answer[0], answer[1])
            answers.append(answer)
            reg_mid_exps.append(reg_mid_exp)
            exp_num += 1
    # 保存生成的表达式和答案
    with open(r"Exercises.txt", 'w+') as e_file:
        for i in range(n):
            e_file.write('{:d}. {}\n'.format(i+1, ' '.join(list(map(str, mid_exps[i])))))
    with open(r'Answers.txt', 'w+') as a_file:
        for i in range(n):
            a_file.write('{:d}. {}\n'.format(i+1, str(answers[i])))

"""
评分
"""
def grade(exp_filename, a_filename):
    dirname = re.sub(exp_filename, '', os.path.abspath(exp_filename))
    correct = []
    wrong = []
    with open(dirname + 'Answers.txt') as file:
        right_answers = file.readlines()
    with open(a_filename) as file:
        answers = file.readlines()
    for i in range(len(right_answers)):
        r_answer = re.split('\s+', right_answers[i])[1]
        answer = re.split('\s', answers[i])[1]
        if r_answer == answer:
            correct.append(i+1)
        else:
            wrong.append(i+1)
    with open('Grade.txt', 'w+') as file:
        file.write('Correct：{:d} ({})\n'.format(len(correct), ','.join(list(map(str, correct)))))
        file.write('Wrong：{:d} ({})\n'.format(len(wrong), ','.join(list(map(str, wrong)))))


if __name__ == '__main__':
    args = sys.argv
    # 判断输入的参数格式是否符合要求
    if ((('-r' not in args or '-n' not in args) and ('-e' not in args or '-a' not in args)) or len(args) != 5
        or (args[1] not in ['-e','-a','-r','-n'] or args[3] not in ['-e','-a','-r','-n'])):
        print('the format of the parameters is error')
        sys.exit(0)
    else:
        if '-n' in args:
            try:    # 判断参数值类型是否正确
                args[2] = int(args[2]); args[4] = int(args[4])
            except:
                print('the type of the parameters is error')
                sys.exit(0)
            if args[2] <= 0 or args[4] <= 0: # 判断参数值范围是否张雀
                print('the value of the parameters is error')
                sys.exit(0)
            # 生成表达式
            if args[1] == '-n':
                n = args[2]; r = args[4]
            else:
                n = args[4]; r = args[2]
            generate_expressions(n, r)
            print('generate expressions done.')
        else:
            exp_filename = args[2]
            a_filename = args[4]
            if not os.path.exists(exp_filename) or not os.path.exists(a_filename):
                print('the file is not found')
                sys.exit(0)
            elif not os.path.exists(re.sub(exp_filename, '', os.path.abspath(exp_filename)) + 'Answers.txt'):
                print('the correct answer file is not found')
                sys.exit(0)
            else:
                grade(exp_filename, a_filename)
                print('generate grade file done.')

