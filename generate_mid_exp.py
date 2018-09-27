import random


"""
随机生成题目数量为n，数值在r以内的四则运算表达式
parameters:
    n(int)：四则运算表达式的个数
    r(int)：操作数的值上界
return:
    mid_exps(list)：存储中缀表达式的列表
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

    # 操作符只存在 + 或 *，进行特殊处理
    select_operators_set = set(select_operators)
    op = select_operators_set.copy().pop()
    reg_mid_exp = None
    expression_value = None
    if len(select_operators_set) == 1 and op in ['+', '*']:
        reg_mid_exp = list(map(str, sorted(datas, reverse=True)))
        expression_value = datas[0]
        for i in range(len(reg_mid_exp)-1):
            reg_mid_exp.insert(i*2+1, op)
            if op == '+':
                expression_value = expression_value + datas[i+1]
            else:
                expression_value = expression_value * datas[i+1]
    # 生成中缀表达式
    mid_exp = [datas[-1]]
    for i in range(data_num - 1):
        mid_exp.append(select_operators[i])
        mid_exp.append(datas[i])
    mid_exp = add_bracket(mid_exp, len(datas)) # 以33%的概率随机生成括号
    if reg_mid_exp == None:         # 操作符随机的情况
        return mid_exp, None, None
    else:                           # 操作符全为 + 或 * 的情况
        return mid_exp, ' '.join(reg_mid_exp), (expression_value,1)

"""
以33%的概率，给生成的表达式加上括号
parameters:
    mid_exp(list)：随机生成的表达式
    data_num(int)：操作数个数
return:
    mid_exp(list)：处理后的中缀表达式
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