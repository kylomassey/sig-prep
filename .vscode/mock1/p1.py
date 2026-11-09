def breaches(parent, exposure, limit):
    n = len(parent)
    breach = exposure[:]
    ans = []

    for i in range(n):
        idx = parent[i]
        total = exposure[i]
        while idx != -1:
            breach[idx] += total
            idx = parent[idx]
    for i in range(n):
        if breach[i] > limit[i]:
            ans.append(i)
    return ans
print(breaches(parent=[-1, 0, 0, 1, 1],
         exposure=[10, 20, -5, 15, 30],
         limit=[100, 60, 0, 20, 25]))