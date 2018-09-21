"""
将生成的表达式二叉树转化为中缀表达式
用于判断随机生成的四则运算表达式是否重复
parameters:
    exp_tree(dict)：表达式二叉树
return:
    exp_mid(str)：规范的中缀表达式
"""
def exp_tree_to_mid_exp(exp_tree):
    (key, child), = exp_tree.items()  # 获取子树

    if type(child[0]) == type(1) or type(child[0]) == type(0.1):
        mid_exp = '(' + str(child[0])
    else:
        mid_exp = '(' + str(exp_tree_to_mid_exp(child[0]))
    mid_exp += " " + key + " "
    if type(child[1]) == type(1) or type(child[1]) == type(0.1):
        mid_exp += str(child[1]) + ')'
    else:
        mid_exp += str(exp_tree_to_mid_exp(child[1])) + ')'
    return mid_exp