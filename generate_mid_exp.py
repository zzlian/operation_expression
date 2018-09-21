import random


"""
随机生成题目数量为n，数值在r以内的四则运算表达式
parameters:
    n(int)：四则运算表达式的个数
    r(int)：操作数的值上界
return:
    mid_exps(list)：中缀表达式列表
"""
def generate_mid_exp(max_num):
    data_num = random.randint(2, 4)     # 操作数个数
    datas = []                          # 操作数
    operators = ['+', '-', '*', '/']
    select_operators = []               # 操作符

    for i in range(data_num):          # 随机生成操作数
        data = int(random.random() * max_num)
        datas.append(data)
    for i in range(data_num - 1):      # 随机生成操作符
        operator = operators[int(random.random() * 4)]
        select_operators.append(operator)

    mid_exp = [datas[-1]]
    for i in range(data_num - 1):      # 生成中缀表达式
        mid_exp.append(select_operators[i])
        mid_exp.append(datas[i])
    mid_exp = add_bracket(mid_exp, len(datas))
    return mid_exp

"""
以33%的概率，给生成的表达式加上括号
parameters:
    mid_exp(str)：随机生成的表达式
    data_num(int)：操作数个数
return:
    mid_exp(str)：处理的中缀表达式
"""
def add_bracket(mid_exp, data_num):
    # 为生成的表达式加括号
    if data_num == 3:  # 操作数个数为3时的加括号方式
        bracket_way = random.randint(0, 4)
        prob = [0, 1, 0, 2, 0, 0]  # 以33%的概率加上括号，67%的概率不加括号
        bracket_way = prob[bracket_way]
        if bracket_way == 1:
            mid_exp.insert(0, '(')
            mid_exp.insert(4, ')')
        elif bracket_way == 2:
            mid_exp.insert(2, '(')
            mid_exp.append(')')
    elif data_num == 4:  # 操作数个数为4时的加括号方式
        bracket_way = random.randint(0, 5)
        prob = [0, 0, 1, 0, 0, 2, 0, 3, 0, 0, 4, 0, 5, 0, 0]  # 以33%的概率加括号,以67%的概率不加括号
        if bracket_way == 1:
            mid_exp.insert(0, '(')
            mid_exp.insert(4, ')')
        elif bracket_way == 2:
            mid_exp.insert(2, '(')
            mid_exp.insert(6, ')')
        elif bracket_way == 3:
            mid_exp.insert(4, '(')
            mid_exp.append(')')
        elif bracket_way == 4:
            mid_exp.insert(0, '(')
            mid_exp.insert(6, ')')
        elif bracket_way == 5:
            mid_exp.insert(2, '(')
            mid_exp.append(')')
    return mid_exp