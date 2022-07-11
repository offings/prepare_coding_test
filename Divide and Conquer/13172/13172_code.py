from math import gcd
x = 1000000007
ans = 0

def divide_mod(n, mod):
    if mod == 1: return n
    half = divide_mod(n, mod // 2)
    if mod % 2:
        return n * half * half % x
    return half * half % x
    

m = int(input())
for _ in range(m):
    n, s = map(int, input().split())
    g = gcd(n, s)
    n //= g
    s //= g

    ans += s * divide_mod(n, x - 2) % x
    ans %= x

print(ans)



