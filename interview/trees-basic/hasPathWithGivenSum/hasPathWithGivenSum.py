#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def hasPathWithGivenSum(t, s):
    return preorder(t, 0, s)


def preorder(node, current_sum, goal_sum):
    if not node:
        return False

    current_sum += node.value
    if node.left and preorder(node.left, current_sum, goal_sum):
        return True
    
    if node.right and preorder(node.right, current_sum, goal_sum):
        return True

    if not node.left and not node.right and current_sum == goal_sum:
        return True

    return False
