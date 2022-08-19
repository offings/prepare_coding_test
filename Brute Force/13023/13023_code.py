def dfs(x, depth):
    global is_friend

    visited[x] = True
    if depth == 5:
        print(1)
        exit()

    for c in graph[x]:
        if not visited[c]:
            visited[c] = True
            dfs(c, depth + 1)
            visited[c] = False

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    dfs(i, 1)
    visited[i] = False

print(0)