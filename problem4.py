
def count_streaks(pandl, target):
    cnt = {}
    cumsum = [0]
    total = 0
    for i in pandl:
        cumsum.append(cumsum[-1] + i)
    for i in cumsum:
        a = i - target
        if a in cnt:
            total += cnt[a]
        cnt[i] = cnt.get(i, 0) + 1
    return total
print(count_streaks([1, 2, 3, -3, 3], 3))