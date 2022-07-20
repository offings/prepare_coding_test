from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    in_degree = [-1] + [0] * n
    queue = deque()

    for _ in range(k):
        x, y = map(int, input().split())
        in_degree[y] += 1
        graph[x].append(y)
    
    w = int(input())

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = d[i]

    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            in_degree[next] -= 1
            dp[next] = max(dp[next], dp[cur] + d[next])
            if in_degree[next] == 0:
                queue.append(next)

        if in_degree[w] == 0:
            print(dp[w])
            break
