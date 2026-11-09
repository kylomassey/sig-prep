def vwap_report(feed):
    stock = {}
    ans = []
    for symbol, qty, price in feed:
        if symbol in stock:
            stock[symbol][0] += qty
            stock[symbol][1] += (qty * price)
        else:
            stock[symbol] = [qty, (qty * price)]
    stock = sorted(stock.items())
    print(stock)
    for a, b in stock:
        avg = round(b[1]/b[0],2)
        line = a + " " + f"{avg:.2f}"
        ans.append(line)
    return ans
print(vwap_report([("AAPL", 100, 190.0), ("MSFT", 10, 410.5), ("AAPL", 50, 193.0),
             ("TSLA", 1, 100.0), ("TSLA", 2, 100.01)]))