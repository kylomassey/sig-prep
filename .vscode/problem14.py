from collections import deque

def close_pairs (feed, k):
    if not feed:
        return 0
    feed.sort()
    n = len(feed)
    stack = deque()
    cumsum = ([0] * n)
    for i in range(n):
        while stack and feed[i] - feed[stack[0]] > k:
            stack.popleft()
        if stack:
            cumsum[i] = cumsum[i-1] + i - stack[0]
        else:
            cumsum[i] = cumsum[i-1]
        stack.append(i)
    return cumsum[-1]
assert close_pairs([],2) == 0
assert close_pairs([1,5],3) == 0
assert close_pairs([1,2],3) == 1