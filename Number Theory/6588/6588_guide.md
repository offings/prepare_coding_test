## 백준 6588 골드바흐의 추측
[문제 링크](https://www.acmicpc.net/problem/6588)

## 문제
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

이 추측은 아직도 해결되지 않은 문제이다.

백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

## 핵심 포인트
```
- 테스트 케이스가 최대 100,000개이므로 에라토스테네스의 체 결과는 전역 변수로 저장하는 것이 접근하기 편리하다.
- n을 만들 수 있는 방법 중 가장 차이가 큰 것을 출력해야 하므로 가장 작은 소수이자 홀수인 3부터 값 비교를 시작한다.
```

## 핵심 코드
```
max_val = 1000000
check_prime = [False, False] + [True] * (max_val - 1)

# 에라토스테네스의 체를 실행하여 소수 판별
for i in range(2, int(max_val ** 0.5) + 1):
    if check_prime[i]:
        for j in range(i * 2, max_val + 1, i):
            check_prime[j] = False

while True:
    flag = 0
    n = int(input())
    if n == 0: break

    # n을 만들 수 있는 방법이 여러가지라면 차이가 가장 큰 것을 출력하라고 했으므로
    # 가장 작은 소수와 홀수인 3부터 시작
    for i in range(3, n + 1, 2):
	# 합이 n인 두 수가 모두 소수이면 값 출력
        if check_prime[i] and check_prime[n - i]:
            print(f'{n} = {i} + {n - i}')
            flag = 1
            break

    # 골드바흐의 추측이 틀렸다면 아래 문구 출력
    if not flag:
        print('Goldbach''s conjecture is wrong.')
```
