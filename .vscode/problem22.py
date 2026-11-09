import heapq

def settle_order(k, orders):
    needs = []
    needsb = [[0,i] for i in range(k)]
    wanted = {}
    ans = []
    for a, b in orders:
        if a in wanted:
            wanted[a].append(b)
        else:
            wanted[a] = [b]
        needsb[b][0] += 1

    heapq.heapify(needs)
    for a, b in needsb:
        if a == 0:
            heapq.heappush(needs,b)
    while needs:
        b = heapq.heappop(needs)
        ans.append(b)
        if b not in wanted:
            continue
        for c in wanted[b]:
            needsb[c][0] -= 1
            if needsb[c][0] == 0:
                heapq.heappush(needs, c)
    return ans if len(ans) == k else []

print(settle_order(4, [(1, 0)]) )
