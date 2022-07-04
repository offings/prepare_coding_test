import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if paper[nx][ny] >= 1:
                        paper[nx][ny] += 1
                    else:
                        visited[nx][ny] = True
                        queue.append([nx, ny])

n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while True:
    visited = [[False] * m for _ in range(n)]
    flag = 0
    bfs()

    for i in range(n):
        for j in range(m):
            if paper[i][j] >= 3:
                paper[i][j] = 0
                flag = 1
            elif paper[i][j] == 2:
                paper[i][j] = 1

    if flag:
        time += 1
    else:
        break

print(time)


