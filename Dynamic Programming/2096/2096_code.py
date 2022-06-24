import sys
input = sys.stdin.readline

n = int(input())

min_prev = [0] * 3
min_cur = [0] * 3
max_prev = [0] * 3
max_cur = [0] * 3

for i in range(n):
    mat = list(map(int, input().split()))
    min_cur[0] = mat[0] + min(min_prev[0], min_prev[1])
    min_cur[1] = mat[1] + min(min_prev)
    min_cur[2] = mat[2] + min(min_prev[1], min_prev[2])

    max_cur[0] = mat[0] + max(max_prev[0], max_prev[1])
    max_cur[1] = mat[1] + max(max_prev)
    max_cur[2] = mat[2] + max(max_prev[1], max_prev[2])

    for j in range(3):
        min_prev[j] = min_cur[j]
        max_prev[j] = max_cur[j]
    
print(max(max_cur), min(min_cur))