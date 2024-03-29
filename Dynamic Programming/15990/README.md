## 백준 15990 1, 2, 3 더하기 5
[문제 링크](https://www.acmicpc.net/problem/15990)

## 문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 3가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 단, 같은 수를 두 번 이상 연속해서 사용하면 안 된다.

- 1+2+1
- 1+3
- 3+1   

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

## 핵심 포인트
```
- 같은 수를 두 번 이상 연속해서 사용되지 않도록 점화식을 구성한다.
- 이차원 배열을 이용해서 각각 1, 2, 3으로 연산이 끝날 경우를 구해 배열에 저장한다. 시간 초과를 해결하기 위해 배열에 저장할 때도 나머지 연산을 수행한다.
```

## 핵심 코드
```
# 모든 값에 대해 1로 끝나는 경우, 2로 끝나는 경우, 3으로 끝나는 경우를 모두 저장
dp = [[0] * 4 for _ in range(100001)]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

# 4부터는 dp 배열에 저장된 값을 바탕으로 값 누적
for i in range(4, 100001):
    # 1로 끝나는 경우는 자신보다 1 작은 수에서 2로 끝나는 경우와 3으로 끝나는 경우의 합
    dp[i][1] = dp[i - 1][2] % max + dp[i - 1][3] % max
    # 2로 끝나는 경우는 자신보다 2 작은 수에서 1로 끝나는 경우와 3으로 끝나는 경우의 합
    dp[i][2] = dp[i - 2][1] % max + dp[i - 2][3] % max
    # 3으로 끝나는 경우는 자신보다 3 작은 수에서 1로 끝나는 경우와 2로 끝나는 경우의 합
    dp[i][3] = dp[i - 3][1] % max + dp[i - 3][2] % max

```
