import heapq

def min_conversions(pairs, cur1, cur2):
    pos = {cur1:0, cur2:1}
    links = [[] for _ in range(len(pairs) * 2)]
    cnt = 2
    for a, b in pairs:
        if a not in pos:
            pos[a] = cnt
            cnt += 1
        if b not in pos:
            pos[b] = cnt
            cnt += 1
        links[pos[a]].append(pos[b])
        links[pos[b]].append(pos[a])
    heap = [(0, pos[cur1])]
    best = float('inf')
    while heap:
        c, d = heapq.heappop(heap)
        print("cost:", c)

        if pos[cur2] == d:
            return c
        if c > len(pairs):
            return -1 
        for curr in links[d]:
            heapq.heappush(heap, (c + 1,curr))
    return -1
        
pairs = [("USD", "EUR"), ("EUR", "GBP"), ("GBP", "JPY"),
         ("USD", "CAD"), ("CAD", "JPY")]

print(min_conversions(pairs, "USD", "JPY"))  # → 2   (USD → CAD → JPY)
print(min_conversions(pairs, "EUR", "CAD"))  # → 2   (EUR → USD → CAD)
min_conversions(pairs, "USD", "CHF")  # → -1  (CHF isn't reachable)