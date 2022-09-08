n, m, r = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

pa = [[0] * 100 for _ in range(100)]
oper = list(map(int, input().split()))

for o in oper:
    if o == 1:
        for i in range(n - 1, -1, -1):
            for j in range(m):
                pa[(n - 1) - i][j] = a[i][j]

    elif o == 2:
        for i in range(n):
            for j in range(m - 1, -1, -1):
                pa[i][(m - 1) - j] = a[i][j]

    elif o == 3:
        for i in range(n):
            for j in range(m):
                pa[j][(n - 1) - i] = a[i][j]
        n, m = m, n

    elif o == 4:
        for i in range(n):
            for j in range(m):
                pa[(m - 1) - j][i] = a[i][j]
        n, m = m, n

    elif o == 5:
        half_row = n // 2
        half_col = m // 2

        for i in range(half_row):
            for j in range(half_col):
                pa[i][j + half_col] = a[i][j]

        for i in range(half_row):
            for j in range(half_col, m):
                pa[i + half_row][j] = a[i][j]

        for i in range(half_row, n):
            for j in range(half_col, m):
                pa[i][j - half_col] = a[i][j]

        for i in range(half_row, n):
            for j in range(half_col):
                pa[i - half_row][j] = a[i][j]
    else:
        half_row = n // 2
        half_col = m // 2

        for i in range(half_row):
            for j in range(half_col):
                pa[i + half_row][j] = a[i][j]

        for i in range(half_row):
            for j in range(half_col, m):
                pa[i][j - half_col] = a[i][j]

        for i in range(half_row, n):
            for j in range(half_col, m):
                pa[i - half_row][j] = a[i][j]

        for i in range(half_row, n):
            for j in range(half_col):
                pa[i][j + half_col] = a[i][j]

    a = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = pa[i][j]

for i in range(n):
    for j in range(m):
        print(pa[i][j], end = ' ')
    print()

