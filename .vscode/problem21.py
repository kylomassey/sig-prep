
def all_fills(lots, fill):
    lots = sorted(lots, key=lambda x:x)
    ans = []
    n = len (lots)
    def dive(idx = 0, order = [], size = fill):
        if size == 0:
            ans.append(order)
        elif size < 0:
            return
        for i in range(idx, n):
            dive(i, order + [lots[i]], size - lots[i])

    dive()
    return ans

print(all_fills([2, 3, 5], 8))