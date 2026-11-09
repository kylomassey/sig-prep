def max_profit(feed, fee):
    low = float('inf')
    best = 0
    for price in feed:
        if price < low:
            low = price
        elif price - low - fee > 0:
            best += price - low - fee
            low = price-fee
    return best
assert max_profit([], 2) == 0
assert max_profit([1,3], 0) == 2
assert max_profit([3,1], 4) == 0
print(max_profit([5,4,3,2,1,4,5],2))
print(max_profit([1, 3, 2, 8, 4, 9], 2))