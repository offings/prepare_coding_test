from collections import deque
n, k = map(int, input().split())
max = 100001
dist = [-1] * max
last = [i for i in range(max)]

def bfs(s):
    queue = deque()
    queue.append(s)
    dist[s] = 0
    last[s] = -1

    answer = []
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            while last[x] != -1:
                answer.append(x)
                x = last[x]
            answer.append(x)
            print(*answer[::-1])
            break

        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx < max and dist[nx] == -1:
                queue.append(nx)
                last[nx] = x
                dist[nx] = dist[x] + 1

bfs(n)