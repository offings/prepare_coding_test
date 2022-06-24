import sys
input = sys.stdin.readline

def bellman_ford(s):
    global n

    dist[s] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for next, next_cost in graph[j]:
                if dist[j] != INF and dist[next] > dist[j] + next_cost:
                    dist[next] = dist[j] + next_cost

                    if i == n:
                        return True

    return False

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = int(1e9)
dist = [INF] * (n + 1)
negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
