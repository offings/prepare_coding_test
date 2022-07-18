n, m, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
answer = -int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def back_tracking(rx, ry, cnt, val):
    global answer
    if cnt == k:
        answer = max(answer, val)
        return

    else:
        for x in range(rx, n):
            for y in range(ry if x == rx else 0, m):
                if visited[x][y]:
                    continue
                
                flag = 1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                        flag = 0
                        break

                if flag:
                    visited[x][y] = True
                    back_tracking(x, y, cnt + 1, val + board[x][y])
                    visited[x][y] = False


back_tracking(0, 0, 0, 0)
print(answer)
