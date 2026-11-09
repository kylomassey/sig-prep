def find(parent, x):
    while parent[x]!= x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def largest_cluster(n, feed, limit):
    parent = [i for i in range(n)]
    for a, b, num in feed:
        if num >= limit:
            ra, rb = find(parent,a), find(parent,b)
            if ra != rb:
                parent[ra]= rb
    high = 0
    freq = {}
    for j in parent:
        freq[j] = freq.get(j, 0) + 1
        high = max(high, freq[j])
    print(parent)
    return high


print(largest_cluster(6, [(0, 4, 500), (1, 2, 50), (2, 3, 700), (3, 4, 800), (4, 5, 100)], 200))