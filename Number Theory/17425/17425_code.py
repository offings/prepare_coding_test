t = int(input())
max_val = 1000000
dp = [1] * (max_val + 1)
s = [0] * (max_val + 1)

for i in range(2, max_val + 1):
    j = 1
    while i * j <= max_val:
        dp[i * j] += i
        j += 1

for i in range(1, max_val + 1):
    s[i] = s[i - 1] + dp[i]

for _ in range(t):
    num = int(input())
    print(s[num])

