#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def kthSmallestInBST(t, k):
    node = t
    while node:
        if not node.left:
            k -= 1
            if k == 0:
                return node.value
            node = node.right
        else:
            pre = node.left
            while pre.right is not None:
                pre = pre.right
            pre.right = node
            node = node.left
            pre.right.left = None
        