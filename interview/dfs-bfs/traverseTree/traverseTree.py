#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def traverseTree(t):
    result = []
    queue = [t]

    while queue:
        current = queue.pop(0)
        if not current:
            continue
        result.append(current.value)
        queue.append(current.left)
        queue.append(current.right)

    return result
