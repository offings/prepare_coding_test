import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))

INF = 100
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j: 
            dist[i][j] = 0


for _ in range(r):
    s, e, c = map(int, input().split())
    dist[s][e] = c
    dist[e][s] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

max_item = 0
for i in range(1, n + 1):
    get_item = 0
    for j in range(1, n + 1):
        if dist[i][j] <= m:
            get_item += items[j]
    max_item = max(max_item, get_item)

print(max_item)
