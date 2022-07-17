r, c, t = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))

for i in range(r):
    if board[i][0] == -1:
        up = i
        down = i + 1
        break

def dust_spread():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    temp = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if board[x][y] != 0 and board[x][y] != -1:
                spread_out = 0

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        temp[nx][ny] += board[x][y] // 5
                        spread_out += board[x][y] // 5

                board[x][y] -= spread_out

    for i in range(r):
        for j in range(c):
            board[i][j] += temp[i][j]


def up_circle():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    dir, temp = 0, 0
    x, y = up, 1

    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if x == up and y == 0:
            break

        if 0 > nx or nx >= r or 0 > ny or ny >= c:
            dir += 1
            continue

        board[x][y], temp = temp, board[x][y]
        x = nx
        y = ny

def down_circle():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    dir, temp = 0, 0
    x, y = down, 1

    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if x == down and y == 0:
            break

        if 0 > nx or nx >= r or 0 > ny or ny >= c:
            dir += 1
            continue

        board[x][y], temp = temp, board[x][y]
        x = nx
        y = ny

for _ in range(t):
    dust_spread()
    up_circle()
    down_circle()

answer = 0
for i in range(r):
    answer += sum(board[i])
print(answer + 2)