a, b = map(int, input().split())

cnt = 1
while True:
    if b == a:
        print(cnt)
        break
    elif b < a or (str(b)[-1] != '1' and b % 2 != 0):
        print(-1)
        break
    else:
        if str(b)[-1] == '1':
            b //= 10
            cnt += 1
        else:
            b //= 2
            cnt += 1
