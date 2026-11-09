def allocate(buy, sell, budget):
    n = len(buy)
    ans = 0
    for mask in range(1 << n):
        total = 0
        profit = 0
        for i in range(n):
            if mask & (1 << i):
                total += buy[i]
                if total > budget:
                    break
                profit += sell [i]
            ans = max(profit, ans)
    return ans

print(allocate([1, 3, 4, 5], [1, 4, 5, 7], 7))