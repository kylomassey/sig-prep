def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def group_counts(k, links):
    parent = [i for i in range(k)]
    ans = []
    cnt = k
    for a, b in links:
        ra, rb = find(parent,a), find(parent,b)
        if ra != rb:
            parent[ra] = rb
            cnt -= 1
        ans.append(cnt)
    return ans

print(group_counts(3, [(0, 1), (2, 1)]) )