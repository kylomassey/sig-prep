def fill_order (lots, target):
    n = len(lots)
    dp = [0] + ([-1] * target)
    for i in range(target + 1):
        for lot in lots:
            if i < lot:
                continue
            elif dp[i % lot] > 0:
                if dp[i % lot] == -1:
                    continue
                if dp[i] == -1:
                    dp[i] = dp[i % lot] + i // lot
                else:
                    dp[i] = min(dp[i], dp[i % lot] + i // lot)
            elif i % lot == 0:
                if dp[i] == -1:
                    dp[i] = i // lot
                else:
                    dp[i] = min(dp[i], i // lot)
    return dp[-1]
assert fill_order([],10) == -1
assert fill_order([5,2],0) == 0
assert fill_order([1,5],5) == 1
print(fill_order([1, 3, 4], 6))