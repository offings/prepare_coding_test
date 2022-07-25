n = int(input())
sign_matrix = list(input())
sign = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        s = sign_matrix.pop(0)
        if s == '+':
            sign[i][j] = 1
        elif s == '-':
            sign[i][j] = -1

result = []

def is_possible(count):
    total = 0
    for i in range(count, -1, -1):
        total += result[i]
        if total > 0 and sign[i][count] <= 0:
            return False
        elif total == 0 and sign[i][count] != 0:
            return False
        elif total < 0 and sign[i][count] >= 0:
            return False
    return True

def back_tracking(count):
    if count == n:
        print(' '.join(map(str, result)))
        exit(0)

    for i in range(1, 11):
        real_i = sign[count][count] * i
        result.append(real_i)
        if is_possible(count):
            back_tracking(count + 1)
        result.pop()

back_tracking(0)