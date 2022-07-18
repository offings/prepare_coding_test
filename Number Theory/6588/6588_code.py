max_val = 1000000
check_prime = [False, False] + [True] * (max_val - 1)

for i in range(2, int(max_val ** 0.5) + 1):
    if check_prime[i]:
        for j in range(i * 2, max_val + 1, i):
            check_prime[j] = False

while True:
    flag = 0
    n = int(input())
    if n == 0: break

    for i in range(3, n + 1, 2):
        if check_prime[i] and check_prime[n - i]:
            print(f'{n} = {i} + {n - i}')
            flag = 1
            break

    if not flag:
        print('Goldbach''s conjecture is wrong.')