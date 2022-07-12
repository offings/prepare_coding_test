import heapq
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(r):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])
    graph[e].append([s, c])

def dijstra(s):
    global dist
    queue = []
    heapq.heappush(queue, [0, s])
    dist = [100] * (n + 1)
    dist[s] = 0

    while queue:
        now_cost, now = heapq.heappop(queue)
        if now_cost > dist[now]:
            continue

        for next, next_cost in graph[now]:
            cost = now_cost + next_cost
            if dist[next] > cost:
                dist[next] = cost
                heapq.heappush(queue, [cost, next])

    return dist

get_items = [0] * (n + 1)
for i in range(1, n + 1):
    dist = dijstra(i)
    for j in range(1, n + 1):
        if dist[j] <= m:
            get_items[i] += items[j]

print(max(get_items))