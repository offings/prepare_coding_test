n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0] + [0] * n

for i in range(1, n + 1):
    dp[i] = p[i]
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[-1])