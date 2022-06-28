import heapq
import sys
input = sys.stdin.readline

def dijkstra(s):
    dist = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue, (0, s))
    dist[s] = 0

    while queue:
        now_dist, now = heapq.heappop(queue)

        if dist[now] < now_dist:
            continue

        for next, next_dist in graph[now]:
            cost = now_dist + next_dist
            if dist[next] > cost:
                dist[next] = cost
                heapq.heappush(queue, (cost, next))

    return dist

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = int(1e9)
result = []
for i in range(1, n + 1):
    result.append(dijkstra(i))

for i in range(n):
    for j in range(1, n + 1):
        if result[i][j] == INF:
            result[i][j] = 0
            
for i in range(n):
    print(*result[i][1:])