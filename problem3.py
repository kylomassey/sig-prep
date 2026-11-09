
def pnl_report(fills, close):
    ans = []
    track = {}
    for fill in fills:
        if fill[1] == 'B':
            mod = -1
        else:
            mod = 1
        ticker = fill[0]
        price = fill[2] * fill[3]
        if track.get(ticker,0) != 0:
            track[ticker]["price"] += (price*mod)
            track[ticker]["pos"] += (fill[2] * mod * -1)
            track[ticker]["maxpos"] = max(track[ticker]["maxpos"], abs(track[ticker]["pos"]))
        else:
            track[ticker] = {"price":(price*mod), "pos":(fill[2] * mod * -1), "maxpos":fill[2]}
    for c in sorted(track):
        track[c]["price"] = (track[c]["pos"] * close[c]) + track[c]["price"]
        ans.append((c, track[c]["pos"], track[c]["price"], track[c]["maxpos"]))
    return ans

fills = [
    ("AAPL", "B", 10, 100),
    ("MSFT", "B", 5, 200),
    ("AAPL", "S", 4, 105),
    ("MSFT", "S", 5, 190),
    ("AAPL", "B", 2, 98),
]
close = {"AAPL": 103, "MSFT": 195}
pnl_report(fills,close)