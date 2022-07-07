import heapq
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])

start, end = map(int, input().split())

dist = [int(1e9)] * (n + 1)
near = [start] * (n + 1)

def dijstra(s):
    queue = []
    heapq.heappush(queue, [0, s])
    dist[s] = 0

    while queue:
        now_cost, now = heapq.heappop(queue)

        if now_cost > dist[now]:
            continue

        for next, next_cost in graph[now]:
            cost = now_cost + next_cost
            if dist[next] > cost:
                dist[next] = cost
                near[next] = now
                heapq.heappush(queue, [cost, next])

dijstra(start)
print(dist[end])

temp = end
near_list = []
while temp != start:
    near_list.append(temp)
    temp = near[temp]
near_list.append(temp)
near_list.reverse()

print(len(near_list))
print(*near_list)
