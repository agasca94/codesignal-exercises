def feedingTime(classes):
    classes = [set(animals) for animals in classes]
    # Create adjacency list between classes that have animals in common
    graph = [
        [
            c2 for c2 in range(len(classes))
            # Check if classes 1 and 2 have animals in common
            # by making an intersection between the animals sets
            if c1 != c2 and classes[c1] & classes[c2]
        ]
        for c1 in range(len(classes))
    ]

    colorings = [None] * len(classes)
    for k in range(1, 6):
        res = helper(0, 1, colorings, graph, k)
        if res:
            return k

    return -1


def helper(node, color, colorings, graph, k):
    if node == len(colorings) - 1:
        return True

    colorings[node] = color

    next_node = node + 1
    adjacent_colors = set()

    # Save all the colors used by the neighbors of the next node
    for neighbor in graph[next_node]:
        if colorings[neighbor]:
            adjacent_colors.add(colorings[neighbor])

    for color in range(1, k + 1):
        # Discard any color currently used by a neighbor
        if color in adjacent_colors:
            continue
        res = helper(next_node, color, colorings, graph, k)
        if res:
            return True

    colorings[node] = None

    return False
