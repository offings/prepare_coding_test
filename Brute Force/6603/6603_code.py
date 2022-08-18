from itertools import combinations

while True:
    array = list(map(int, input().split()))
    k = array[0]

    if k == 0:
        break
    else:
        s = array[1:]

    comb = combinations(s, 6)
    for c in comb:
        print(*c)
    print()
