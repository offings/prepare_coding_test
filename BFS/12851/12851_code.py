from collections import deque
n, k = map(int, input().split())
max_val = 100001
dist = [-1] * (max_val)

def bfs(s):
    min_cnt = 0
    queue = deque()
    queue.append(s)
    
    dist[s] = 0

    while queue:
        now = queue.popleft()

        if now == k:
            min_cnt += 1

        for next in [now - 1, now + 1, now * 2]:
            if 0 <= next < max_val:
                if dist[next] == -1 or dist[next] == dist[now] + 1:
                    dist[next] = dist[now] + 1
                    queue.append(next)

    return min_cnt

min_cnt = bfs(n)
print(dist[k])
print(min_cnt)