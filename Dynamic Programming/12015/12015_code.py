import bisect
import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
dp = [num_list[0]]

for i in range(1, n):
    if num_list[i] > dp[-1]:
        dp.append(num_list[i])
    else:
        idx = bisect.bisect_left(dp, num_list[i])
        dp[idx] = num_list[i]

print(len(dp))