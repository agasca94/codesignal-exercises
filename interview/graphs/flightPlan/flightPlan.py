from heapq import heappush, heappop


def flightPlan(times, source, d):
    arrivals = {}
    graph = {}
    for src, dest, departure, arrival in times:
        if src not in arrivals:
            arrivals[src] = 'A'
        if dest not in arrivals:
            arrivals[dest] = 'A'
        if src not in graph:
            graph[src] = {dest: [(departure, arrival)]}
        else:
            if dest in graph[src]:
                graph[src][dest].append((departure, arrival))
            else:
                graph[src][dest] = [(departure, arrival)]
    
    if d not in arrivals:
        return "-1"

    arrivals[source] = '00:00'
    heap = []
    heappush(heap, (arrivals[source], source))
    while heap:
        arrival, current = heappop(heap)
        if current == d:
            break
        if current not in graph:
            continue
        for dest in graph[current]:
            for departure, next_arrival in graph[current][dest]:
                if arrival != '00:00' and not helper(arrival, departure):
                    continue
                if arrivals[dest] > next_arrival:
                    arrivals[dest] = next_arrival
                    heappush(heap, (next_arrival, dest))

    return arrivals[d] if arrivals[d] != 'A' else "-1"


def helper(arrival, departur):
    a_h, a_m = map(int, arrival.split(':'))
    d_h, d_m = map(int, departur.split(':'))

    return d_h > a_h and (d_h - a_h > 1 or d_m >= a_m)
