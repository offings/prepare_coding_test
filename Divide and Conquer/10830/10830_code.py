import sys
input = sys.stdin.readline

n, b = map(int, input().split())
p = 1000
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

def mul(mat1, mat2):
    res = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            for k in range(n):
                res[row][col] += (mat1[row][k] * mat2[k][col])
            res[row][col] %= p
    return res

def divide_square(mat, b):
    if b == 1:
        for row in range(n):
            for col in range(n):
                mat[row][col] %= p
        return mat

    temp = divide_square(mat, b // 2)
    if b % 2: 
        return mul(mul(temp, mat), temp)
    else:
        return mul(temp, temp)

res = divide_square(mat, b)
for i in range(n):
    print(*res[i])