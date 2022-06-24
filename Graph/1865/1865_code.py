import sys
input = sys.stdin.readline

def bellman_ford():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for next, next_cost in graph[j]:
                if dist[next] > dist[j] + next_cost:
                    dist[next] = dist[j] + next_cost

                    if i == n:
                        return True

    return False

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))

    INF = int(1e9)
    dist = [INF] * (n + 1)

    negative_cycle = bellman_ford()
    print('YES' if negative_cycle else 'NO')