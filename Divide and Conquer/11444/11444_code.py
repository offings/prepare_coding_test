n = int(input())
p = 1000000007
mat = [[1, 1], [1, 0]]

def mul(a, b):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += (a[i][k] * b[k][j])
            res[i][j] %= p
    return res

def devide_square(mat, n):
    if n == 1:
        for i in range(2):
            for j in range(2):
                mat[i][j] %= p
        return mat
    
    temp = devide_square(mat, n // 2)
    if n % 2:
        return mul(mul(temp, mat), temp)
    else:
        return mul(temp, temp)

print(devide_square(mat, n)[0][1])