#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def isSubtree(t1, t2):
    return helper(t1, t2) if t2 else True


def helper(t1, t2):
    if not t1 and not t2:
        return True

    if t1 and t2:
        return (
            (
                t1.value == t2.value
            ) and helper(
                t1.left, t2.left
            ) and helper(
                t1.right, t2.right
            )
        ) or (
            helper(t1.left, t2)
        ) or (
            helper(t1.right, t2)
        )

    return False