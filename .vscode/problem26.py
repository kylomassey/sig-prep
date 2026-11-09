import heapq

def cheapest(conv, curr1, curr2):
    idx = {}
    graph = []
    n = 0
    dist = {curr1:0}
    for a, b, d in conv:
        if a not in idx:
            idx[a] = n
            n += 1
            graph.append([[d, b]])
        else:
            graph[idx[a]].append([d,b])
    heap = []
    heapq.heappush(heap, (0, curr1))
    while heap:
        d, u = heapq.heappop(heap)
        if u == curr2:
            return d
        if d > dist[u]:
            continue
        if u not in idx:
            continue
        for a, b in graph[idx[u]]:
            if b not in dist or d + a < dist[b]:
                dist[b] = d + a
                heapq.heappush(heap,[a+d, b])
    return -1

conv = [("USD", "EUR", 3), ("EUR", "JPY", 2), ("USD", "JPY", 10),
        ("USD", "GBP", 1), ("GBP", "JPY", 3)]

print(cheapest(conv, "USD", "JPY"))
print(cheapest(conv, "JPY", "USD"))