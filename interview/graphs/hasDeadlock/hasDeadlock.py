def hasDeadlock(connections):
    memo = [None] * len(connections)
    for node in range(len(connections)):
        res = helper(connections, node, set(), memo)
        memo[node] = res
        if res:
            return True
    return False


def helper(connections, current, path, memo):
    if memo[current] is not None:
        return memo[current]
    if current in path:
        return True
    
    path.add(current)
    for next_node in connections[current]:
        res = helper(connections, next_node, path, memo)
        memo[next_node] = res
        if res:
            return True
    path.remove(current)
    return False
