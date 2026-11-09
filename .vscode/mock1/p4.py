def open_positions(feed):
    stocks = {}

    for line in feed:
        a = line.split(" ")
        if a[2] == 'B':
            stocks[a[1]] = stocks.get(a[1], 0) + int(a[3])
            if stocks[a[1]] == 0:
                stocks.pop(a[1])
        elif a[2] == 'S':
            stocks[a[1]] = stocks.get(a[1], 0) - int(a[3])
            if stocks[a[1]] == 0:
                stocks.pop(a[1])
    ans = []
    stocks = sorted(stocks.items())
    for a, b in stocks:
        entry = a + " " + str(b)
        ans.append(entry)
    return ans
print(open_positions([
    "09:30:01 AAPL B 100 190.5",
    "09:30:02 MSFT S 50 410.0",
    "09:31:00 AAPL S 100 191.0",
    "09:32:10 TSLA B 10 250.25",
    "09:33:00 MSFT S 25 409.5",
]))