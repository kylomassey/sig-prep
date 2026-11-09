import heapq

def merge_feeds(feeds):
    heap = []
    for f, feed in enumerate(feeds):
        print(f,feed)
    heapans = []
    feedlvl = 0
    for feed in feeds:
        num = 0
        for item in feed:
            heapq.heappush(heapans, (item[0], feedlvl, num, item[1]))
            num += 1
        feedlvl += 1
    ans = []
    while heapans:
        cur = heapq.heappop(heapans)
        ans.append((cur[0],cur[1],cur[3]))
    return ans
feeds = [
    [(1, 100), (4, 101), (6, 99)],   # feed 0
    [(2, 50), (3, 51), (6, 52)],     # feed 1
    [(5, 200)],                      # feed 2
]
print(merge_feeds(feeds))