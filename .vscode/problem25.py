def longest_focus(feed, k):
    seen = {}
    d = 0
    ans = 0
    l = 0
    n = len(feed)
    for r in range(n):
        seen[feed[r]] = seen.get(feed[r], 0) + 1
        while len(seen) > k:
            seen[feed[l]] -= 1
            if seen[feed[l]] == 0:
                seen.pop(feed[l])
            l += 1
        d = len(seen)
        ans = max(ans, r - l + 1)
    return ans
longest_focus(["AAPL", "MSFT", "AAPL", "GOOG", "GOOG", "AAPL", "TSLA"], 2) 