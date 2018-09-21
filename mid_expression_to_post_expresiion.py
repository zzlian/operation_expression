"""
将中缀表达式转化为后缀表达式
parameters:
    exp_mid(list)：中缀表达式
return:
    exp_post(list)：后缀表达式
"""
def mid_expression_to_post_expression(exp_mid):
    exp_post = []   # 后缀表达式
    stack = []      # 栈
    operators = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2} # 操作符

    while (len(exp_mid)):
        # 对中缀表达式中的操作符进行处理
        if exp_mid[0] in operators.keys():
            if exp_mid[0] == ')':   # 操作符为右括号
                while True:
                    if stack[len(stack) - 1] == '(':
                        break
                    else:           # 将栈中属于括号内的运算符加入到后缀表达式中
                        exp_post.append(stack.pop())
                stack.pop()         # 删除左括号
            elif len(stack) == 0 or exp_mid[0] == '(' or operators[stack[-1]] < operators[exp_mid[0]]:
                stack.append(exp_mid[0])    # 左括号、优先级高的操作符进栈，或者栈中没有操作符时进栈
            elif operators[stack[-1]] >= operators[exp_mid[0]]:
                while operators[stack[-1]] >= operators[exp_mid[0]]:
                    exp_post.append(stack.pop()) # 将优先级高的运算符出栈处理
                    if len(stack) == 0:
                        break
                stack.append(exp_mid[0])
        # 对中缀表达式中的操作数进行处理
        else:
            exp_post.append(exp_mid[0])        # 将操作数添加到后缀表达式中
        exp_mid = exp_mid[1:]
        if len(exp_mid) == 0:
            while len(stack):
                exp_post.append(stack.pop())
    return exp_post