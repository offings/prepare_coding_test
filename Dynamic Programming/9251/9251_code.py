import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

a_len = len(a)
b_len = len(b)

matrix = [[0] * (b_len + 1) for _ in range(a_len + 1)]

for i in range(1, a_len + 1):
    for j in range(1, b_len + 1):
        if a[i - 1] == b[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[a_len][b_len])