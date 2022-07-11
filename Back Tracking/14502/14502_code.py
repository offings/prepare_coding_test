import sys
input = sys.stdin.readline

n, m = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))
c_room = [[0] * m for _ in range(n)]

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if c_room[nx][ny] == 0:
                c_room[nx][ny] = 2
                spread_virus(nx, ny)

def count_safe():
    c_cnt = 0
    for i in range(n):
        for j in range(m):
            if c_room[i][j] == 0:
                c_cnt += 1

    return c_cnt

def back_tracking(count):
    global answer
    if count == 3:
        for i in range(n):
            for j in range(m):
                c_room[i][j] = room[i][j]

        for i in range(n):
            for j in range(m):
                if c_room[i][j] == 2:
                    spread_virus(i, j)

        c_cnt = count_safe()
        answer = max(c_cnt, answer)
        return

    else:
        for i in range(n):
            for j in range(m):
                if room[i][j] == 0:
                    room[i][j] = 1
                    count += 1
                    back_tracking(count)
                    room[i][j] = 0
                    count -= 1

back_tracking(0)
print(answer)
                