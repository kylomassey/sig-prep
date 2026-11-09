def consolidate(data):
    data = sorted(data, key=lambda x: x[0])
    if not data:
        return []
    n = len(data)
    s = data[0][0]
    e = data[0][1]
    ans = []
    for i in range(n):
        if data[i][0] <= e:
            e = max(e, data[i][1])
        else:
            ans.append((s, e))
            s = data[i][0]
            e = data[i][1]
    return ans + [(s, e)]

assert consolidate([]) == []