from heapq import heappush, heappop


def graphDistances(g, s):
    n = len(g)
    dist = [999] * n
    dist[s] = 0
    heap = []
    heappush(heap, (dist[s], s))
    visited = [0] * n

    while heap:
        d, current = heappop(heap)
        if visited[current]:
            continue
        visited[current] = 1
        for neighbor, weight in enumerate(g[current]):
            if weight == -1 or neighbor == current:
                continue
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heappush(heap, (dist[neighbor], neighbor))

    return dist