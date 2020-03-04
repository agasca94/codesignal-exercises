def singlePointOfFailure(connections):
    backedge, bridges = helper(0, -1, connections, {}, 1)
    return bridges


def helper(node, parent, connections, tree, level):
    tree[node] = level
    highest_backedge = level
    bridges = 0
    for child, has_edge in enumerate(connections[node]):
        if not has_edge or child == parent:
            continue
        if child in tree and tree[child] < highest_backedge:
            # print((node, child), ' is a backedge')
            highest_backedge = tree[child]
        elif child not in tree:
            backedge, subbridges = helper(child, node, connections, tree, level + 1)
            bridges += subbridges
            if backedge > level:
                # print((node, child), ' is a bridge')
                bridges += 1
            elif backedge < highest_backedge:
                highest_backedge = backedge

    return highest_backedge, bridges
