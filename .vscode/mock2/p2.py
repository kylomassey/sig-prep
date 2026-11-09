from collections import deque

def quote_cache(k, feed):
    price = {}
    cache = deque([])
    ans = []
    for line in feed:
        print(cache)
        match line[0]:
            case 'put':
                price[line[1]] = line[2]
            case 'get':
                if line[1] in cache:
                    ans.append(price[line[1]])
                else:
                    ans.append(-1)
        if len(cache) > k:
            cache.popleft()
    return ans
print(quote_cache(2, [("put", "AAPL", 190), ("put", "MSFT", 410), ("get", "AAPL"),
                ("put", "GOOG", 140), ("get", "MSFT"), ("get", "GOOG"),
                ("put", "AAPL", 191), ("get", "AAPL")]))