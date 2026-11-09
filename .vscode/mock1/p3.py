from collections import deque
def rate_limit(feed, k , t):
    traders = {}
    ans = []
    for a, b in feed:
        if b in traders:
            while traders[b] and traders[b][0] <= a - t:
                traders[b].popleft()
            if len(traders[b]) < k:
                traders[b].append(a)
                ans.append(True)
            else:
                ans.append(False)
        else:
            traders[b] = deque([a])
            ans.append(True)
    return ans
print(rate_limit([(1, "a"), (2, "a"), (5, "a"), (13, "a"), (14, "a"), (16, "b")], k=2, t=10))
        

