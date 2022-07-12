from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

result = int(1e6)
for comb in combinations(chicken, m):
    temp = 0
    for h in house:
        each_dist = int(1e6)
        for chi in comb:
            each_dist = min(each_dist, abs(h[0] - chi[0]) + abs(h[1] - chi[1]))
        temp += each_dist
    result = min(result, temp)

print(result)

        