from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, a):
    global n, m
    queue = deque()
    queue.append([x, y, a])
    dist[x][y][a] = 1

    while queue:
        x, y, a = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dist[x][y][a]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if Map[nx][ny] == 0 and not dist[nx][ny][a]:
                    queue.append([nx, ny, a])
                    dist[nx][ny][a] = dist[x][y][a] + 1

                elif Map[nx][ny] == 1 and a == 0:
                    queue.append([nx, ny, 1])
                    dist[nx][ny][1] = dist[x][y][0] + 1

    return -1

n, m = map(int, input().split())
Map = []
for _ in range(n):
    Map.append(list(map(int, input().strip())))

dist = [[[0] * 2 for _ in range(m)] for _ in range(n)]
print(bfs(0, 0, 0))