"""
将后缀表达式转化为二叉树
parameters:
    post_expression(list)：后缀表达式
return:
    expression_tree(dict)：表达式二叉树
"""
def post_expression_to_bitree(post_expression):
    base_node = post_expression.pop()
    exp_tree = {base_node:[]}
    operators = ['+', '-', '*', '/']

    if not post_expression:
        return {}
    # 左子树递归处理
    if post_expression[-1] in operators: # 右子树为操作符
        exp_tree[base_node].append(post_expression_to_bitree(post_expression))
    else:                               # 右子树为操作数
        exp_tree[base_node].append(post_expression.pop())
    # 右子树递归处理
    if post_expression[-1] in operators: # 左子树为操作符
        exp_tree[base_node].insert(0, post_expression_to_bitree(post_expression))
    else:                               # 左子树为操作数
        exp_tree[base_node].insert(0, post_expression.pop())
    return exp_tree

"""
将生成的二叉树进行标准化处理
若左子树表达式的值比右子树表达式的值小，则调换左右子树的位置
parameters:
    exp_tree(dict)：表达式二叉树
return:
    value(float)：表达式的值
    max_value(float)：左右子树中的最大值
    key(str)：当前节点的操作符
"""
def to_reg_exp_tree(exp_tree):
    (key, child), = exp_tree.items()  # 获取子树

    if type(child[0]) == type(1) or type(child[0]) == type(0.1):   # 左子树的操作数
        left_value = (child[0], 1)
        max_lvalue = child[0]
        left_operator = '_'          # 非操作符
    else:                            # 递归规范左子树
        left_value, max_lvalue, left_operator = to_reg_exp_tree(child[0])
        if left_value == None:
            return None, None, None
    if type(child[1]) == type(1) or type(child[1]) == type(0.1):  # 右子树的操作数
        right_value = (child[1], 1)
        max_rvalue = child[1]
        right_operator = '_'
    else:                            # 递归规范右子树
        right_value, max_rvalue, right_operator = to_reg_exp_tree(child[1])
        if right_value == None:
            return None, None, None
    left_value_sub = left_value[0] / left_value[1]
    right_value_sub = right_value[0] / right_value[1]
    # 进行表达式的规范化处理
    if ((max_lvalue < max_rvalue or (left_value_sub < right_value_sub) or (max_lvalue == max_rvalue and
        ((left_operator == '*' and right_operator == '/') or (left_operator != '_' and right_operator == '_'))))
        and key in ['+', '*']):                              # 进行表达式的规范化处理
        exp_tree[key] = [child[1], child[0]]                  # 交换左右子树
        (left_value, right_value) = (right_value, left_value)
    elif left_value_sub < right_value_sub and key == '-':    # 表达式出现负数
        return None, None, None
    # 计算当前子树的最大操作数
    if max_lvalue >= max_rvalue:
        max_value = max_lvalue
    else:
        max_value = max_rvalue
    # 计算表达式的值
    value = calculate(key, left_value, right_value)
    if value == None:             # 表达式中除数出现0的情况
        return None, None, None
    return value, max_value, key

"""
计算字符串表达式的值
parameters:
    operator(str)：操作符
    left_value(float)：表达式的左操作符
    right_value(float)：表达式的右操作符
return:
    result(tuple)：分数组成的元组,第一个值为分子，第二个值为分母
"""
def calculate(operator, left_value, right_value):
    tuple_type = type(())
    if operator == '+':
        if type(left_value) == tuple_type and type(right_value) == tuple_type:
            return (left_value[0]*right_value[1]+right_value[0]*left_value[1], left_value[1]*right_value[1])
        elif type(left_value) == tuple_type and type(right_value) != tuple_type:
            return (left_value[1]*right_value+left_value[0], left_value[1])
        elif type(left_value) != tuple_type and type(right_value) == tuple_type:
            return (left_value*right_value[1]+right_value[0], right_value[1])
        else:
            return (left_value + right_value, 1)
    elif operator == '-':
        if type(left_value) == tuple_type and type(right_value) == tuple_type:
            return (left_value[0]*right_value[1]-right_value[0]*left_value[1], left_value[1]*right_value[1])
        elif type(left_value) == tuple_type and type(right_value) != tuple_type:
            return (left_value[0]-left_value[1]*right_value, left_value[1])
        elif type(left_value) != tuple_type and type(right_value) == tuple_type:
            return (left_value*right_value[1]-right_value[0], right_value[1])
        else:
            return (left_value - right_value, 1)
    elif operator == '*':
        if type(left_value) == tuple_type and type(right_value) == tuple_type:
            return (left_value[0]*right_value[0], left_value[1]*right_value[1])
        elif type(left_value) == tuple_type and type(right_value) != tuple_type:
            return (left_value[0]*right_value, left_value[1])
        elif type(left_value) != tuple_type and type(right_value) == tuple_type:
            return (left_value*right_value[0], right_value[1])
        else:
            return (left_value * right_value, 1)
    elif operator == '/' and right_value[0] != 0:
        if type(left_value) == tuple_type and type(right_value) == tuple_type:
            return (left_value[0]*right_value[1], left_value[1]*right_value[0])
        elif type(left_value) == tuple_type and type(right_value) != tuple_type:
            return (left_value[0], left_value[1]*right_value)
        elif type(left_value) != tuple_type and type(right_value) == tuple_type:
            return (left_value*right_value[1], right_value[0])
        else:
            return (left_value, right_value)
    return None