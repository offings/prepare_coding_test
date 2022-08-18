from itertools import permutations

n = int(input())
w = []

for _ in range(n):
    w.append(list(map(int, input().split())))

num_list = [i for i in range(n)]
perm = list(permutations(num_list, n))

def cal_travel(p):
    cost = 0

    for i in range(n):
        if w[p[i]][p[i + 1]] == 0:
            return int(1e9)
        else:
            cost += w[p[i]][p[i + 1]]

    return cost

min_val = int(1e9)
for p in perm:
    p = list(p)
    p.append(p[0])
    min_val = min(min_val, cal_travel(p))
print(min_val)