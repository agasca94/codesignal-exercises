#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def digitTreeSum(t):
    return helper(t, '')


def helper(node, path):
    path += str(node.value)
    s = 0
    if node.left:
        left_path = helper(node.left, path)
        s += left_path
    if node.right:
        right_path = helper(node.right, path)
        s += right_path
    if not s:
        s = int(path)

    return s