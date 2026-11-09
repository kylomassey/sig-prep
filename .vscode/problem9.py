
def price_span(prices):
    n = len(prices)
    ans = [1] * n
    stack = []
    for i in range(n-1,-1,-1):
        while stack and prices[i] >= prices[stack[-1]]:
            prices[stack[-1]]
            j = stack.pop()
            ans[j] = (j-i)
        stack.append(i)
    return ans
print(price_span([100, 80, 60, 70, 60, 75, 85]))
