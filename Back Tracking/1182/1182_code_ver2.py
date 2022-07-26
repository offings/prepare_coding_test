from itertools import combinations

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

for i in range(1, n + 1):
    comb = combinations(num_list, i)
    for c in comb:
        if sum(c) == s:
            count += 1

print(count)