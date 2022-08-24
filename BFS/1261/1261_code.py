from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global n, m
    queue = deque()
    queue.append([x, y])
    wall[x][y] = 0

    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            print(wall[x][y])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and wall[nx][ny] == -1:
                if maze[nx][ny] == 0:
                    queue.appendleft([nx, ny])
                    wall[nx][ny] = wall[x][y]
                else:
                    queue.append([nx, ny])
                    wall[nx][ny] = wall[x][y] + 1


m, n = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

wall = [[-1] * m for _ in range(n)]
bfs(0, 0)
