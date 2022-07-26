from collections import deque

t = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    dist = [[-1] * l for _ in range(l)]
    dist[x][y] = 0

    while queue:
        x, y = queue.popleft()
        if x == gx and y == gy:
            print(dist[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if dist[nx][ny] == -1:
                    queue.append([nx, ny])
                    dist[nx][ny] = dist[x][y] + 1

for _ in range(t):
    l = int(input())
    kx, ky = map(int, input().split())
    gx, gy = map(int, input().split())

    bfs(kx, ky)