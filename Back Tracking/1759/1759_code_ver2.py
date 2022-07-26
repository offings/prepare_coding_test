from itertools import combinations

l, c = map(int, input().split())
alpha = sorted(input().split())
pw = combinations(alpha, l)

for p in pw:
    cur_vo, cur_con = 0, 0
    for i in range(len(p)):
        if p[i] in ['a', 'e', 'i', 'o', 'u']:
            cur_vo += 1
        else:
            cur_con += 1

    if cur_vo >= 1 and cur_con >= 2:
        print(''.join(p))