def find_digit(num):
    one = 1
    while True:
        if one % num == 0:
            return len(str(one))
        else:
            one = one * 10 + 1

while True:
    try:
        num = int(input())
        print(find_digit(num))

    except:
        break