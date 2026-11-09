def best_basket(cost, returns, budget):
    n = len(cost)
    high = 0
    for mask in range(1 << n):
        total = 0
        c = 0
        for i in range(n):
            if mask & (1 << i):
                    total += returns[i]
                    c += cost[i]
        if c <= budget:
            high = max(high, total)
    print(high)
    return high

assert best_basket([10],[5],0) == 0
assert best_basket([8, 6, 19, 53, 2, 6, 4, 3],[10, 3, 20, 51, 8, 12, 5, 4], 18) == 30