import heapq

def shortest_route(floor):
    x = len(floor)
    y = len(floor[0])
    start = 0
    end = 0
    visited = [[False for _ in range(y)] for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if floor[i][j] == "#":
                visited[i][j] = True
            if floor[i][j] == "S":
                start = [0, i, j]
            if floor[i][j] == "E":
                end = [i, j]
    if not end or not start:
        return -1
    queue = [start]
    while queue:
        dist, a, b = heapq.heappop(queue)
        if end == [a, b]:
            return dist
        if not visited[a][b]:
            visited[a][b] = True
            if a > 0:
                queue.append([dist + 1, a - 1, b])
            if a < x - 1 :
                queue.append([dist + 1, a + 1, b])
            if b > 0:
                queue.append([dist + 1, a, b - 1])
            if b < y - 1:
                queue.append([dist + 1, a, b + 1])
    return -1
assert shortest_route(["SE"]) == 1
assert shortest_route(["S","E"]) == 1
assert shortest_route(["S,#"]) == -1
floor = [
    "S..#",
    "##.#",
    "...E",
]
print(shortest_route(["S","E"]))