from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

perm = list(permutations(a, n))

def cal_abs(p):
    result = 0
    for i in range(n - 1):
        result += abs(p[i] - p[i + 1])
    return result

max_val = -1e9
for p in perm:
    max_val = max(max_val, cal_abs(p))
print(max_val)
