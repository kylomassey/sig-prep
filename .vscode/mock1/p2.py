def max_profit_k(prices, k):
    if not prices or k == 0:
        return 0
    buy = [float("-inf")] * (k + 1)    # buy[j]: best cash while holding, during trade j
    sell = [0] * (k + 1)               # sell[j]: best cash after completing j trades
    for p in prices:
        for j in range(1, k + 1):
            buy[j] = max(buy[j], sell[j - 1] - p)
            sell[j] = max(sell[j], buy[j] + p)
            print(buy)
            print(sell)
            print('\n')
    return sell[k]
print(max_profit_k([3, 2, 6, 5, 0, 3], k=2))