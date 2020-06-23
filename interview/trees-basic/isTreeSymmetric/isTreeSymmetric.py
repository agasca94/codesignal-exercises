#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def isTreeSymmetric(t):
    if t:
        nodes = [t.left, t.right]
        return check_nodes(nodes)
    return True


def check_nodes(nodes):
    values = [node.value if node else None for node in nodes]
    m id = len(values) // 2
    left = values[:mid]
    right = values[mid:][::-1]
    for l, r in zip(left, right):
        if l != r:
            return False
    next_nodes = []
    are_leafs = True
    for node in nodes:
        l = node.left if node else None
        r = node.right if node else None
        next_nodes += [l, r]
        if l or r:
            are_leafs = False

    if are_leafs:
        return True

    return check_nodes(next_nodes)