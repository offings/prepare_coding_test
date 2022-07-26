## 백준 1182 부분수열의 합
[문제 링크](https://www.acmicpc.net/problem/1182)

## 문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

## 핵심 포인트
```
- 조합과 백트래킹을 활용하여 합이 s인 경우를 찾는다.
- 백트래킹을 활용할 경우 현재 숫자 배열의 값을 넣는 경우 재귀, 넣지 않는 경우 재귀 호출을 하면 된다.
- 조합을 활용할 경우 부분 수열의 개수가 1일 때부터 N개까지 반복문을 돌면서 합이 s일 때 count를 증가한다.
```

## 핵심 코드
> 백트래킹을 활용한 부분수열의 합 구하기
```
def back_tracking(idx, total):
    if idx == n:
        if total == s:
            count += 1
        return

    # 현재 숫자 배열의 값을 포함하는 경우
    back_tracking(idx + 1, total + num_list[idx])
    # 현재 숫자 배열의 값을 포함하지 않는 경우
    back_tracking(idx + 1, total)
```
> 조합을 이용한 부분수열의 합 구하기
```
from itertools import combinations

# 부분수열의 개수가 1일 때부터 N까지 모든 경우 구하기
for i in range(1, n + 1):
    comb = combinations(num_list, i)
    # 해당 부분수열의 합이 s일 경우 count 증가
    for c in comb:
        if sum(c) == s:
            count += 1
```
