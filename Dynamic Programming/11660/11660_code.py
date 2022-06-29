import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[0] * (n + 1)]
for _ in range(n):
    matrix.append([0] + list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, n):
        matrix[i][j + 1] += matrix[i][j]

for i in range(1, n):
    for j in range(1, n + 1):
        matrix[i + 1][j] += matrix[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(matrix[x2][y2] - matrix[x1 - 1][y2] - matrix[x2][y1 - 1] + matrix[x1 - 1][y1 - 1])