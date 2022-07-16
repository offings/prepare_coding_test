n = int(input())
pipe = []
for _ in range(n):
    pipe.append(list(map(int, input().split())))

hor = 0
dig = 1
ver = 2
count = 0

def dfs(x, y, dir):
    global count
    if x == n - 1 and y == n - 1:
        count += 1

    if dir == hor or dir == dig:
        if 0 <= (y + 1) < n and not pipe[x][y + 1]:
            dfs(x, y + 1, hor)

    if dir == ver or dir == dig:
        if 0 <= (x + 1) < n and not pipe[x + 1][y]:
            dfs(x + 1, y, ver)

    if 0 <= (x + 1) < n and 0 <= (y + 1) < n:
        if not pipe[x + 1][y] and not pipe[x + 1][y + 1] and not pipe[x][y + 1]:
            dfs(x + 1, y + 1, dig)

dfs(0, 1, hor)
print(count)