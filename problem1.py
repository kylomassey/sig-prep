def rolling_max(prices, k):
    ans = []
    n = len(prices)
    high = prices[0]
    pos = 0
    i = 0
    while i < n:
        if prices[i] > high:
            high = prices[i]
            pos = i
        if i >= k - 1:
            ans.append(high)
        i += 1
        if i >=n:
             break
        if pos < i - k + 1:
            print(i,i-k+1)
            high = prices[i - k + 1]
            for j in range(i - k + 2, i, 1):
                if prices[j] > high:
                        high = prices[j]
                        pos = i
    return ans
print(rolling_max(prices = [1, 3, -1, -3, 5, 3, 6, 7], k = 3))