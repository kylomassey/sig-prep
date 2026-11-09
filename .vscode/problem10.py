def peak_orders(feed):
    n = len(feed)
    times = []
    for x, y in feed:
        times.append([x,0])
        times.append([y,1])
    time = 0
    cur = 0
    best = 0
    enddif = 0
    times = sorted(sorted(times, key= lambda x:x[1]), key= lambda x:x[0])
    for i in range(len(times)):
        if times[i][1] == 0:
            cur +=1
        if time < times[i][0]:
            cur += enddif
            enddif = 0
        if times[i][1] == 1:
            enddif -= 1
        time = times[i][1]
        best = max(best, cur)
    return best
print(peak_orders([[1, 5], [2, 0], [4, 0], [5, 0], [5, 1], [6, 1], [7, 0], [7, 1], [8, 1], [9, 1]]))