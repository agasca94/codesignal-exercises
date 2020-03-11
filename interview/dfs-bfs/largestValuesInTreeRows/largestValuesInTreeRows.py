#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def largestValuesInTreeRows(t):
    current_level = [t]
    results = []

    while current_level:
        m = None
        next_level = []

        for node in current_level:
            if not node:
                continue

            next_level += [node.left, node.right]
            
            if m is None or node.value > m:
                m = node.value

        if m is not None:
            results.append(m)

        current_level = next_level

    return results
