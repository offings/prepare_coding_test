dp = [1]
for i in range(1, 101):
    dp.append(dp[i - 1] * i) 

n, m = map(int, input().split())
print(dp[n] // (dp[n - m] * dp[m]))