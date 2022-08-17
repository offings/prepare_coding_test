## 백준 10819 차이를 최대로
[문제 링크](https://www.acmicpc.net/problem/10819)

## 문제
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

## 핵심 포인트
```
- 기본 백트래킹의 원리, permutations 함수를 이용한 풀이 모두가 가능하다.
- 다만 백트래킹할 때 배열의 값을 비교해서 stack에 추가하는 경우는 오류가 발생한다. 즉, 배열 안에 같은 값이 있을 경우도 고려해야 할 필요가 있다.
```

## 핵심 코드
> 백트래킹을 이용한 풀이 방법
```
visited = [False] * n

# 스택에 있는 값을 차례대로 절댓값 차를 구하고 합
def cal_abs():
    result = 0
    for i in range(n - 1):
        result += abs(stack[i] - stack[i + 1])
    return result

def back_tracking(count):
    global max_val
    # 스택에 포함된 개수가 n개라면 cal_abs 함수 수행 후 최댓값 비교
    if count == n:
        max_val = max(max_val, cal_abs())
        return

    # 스택에 모든 수가 저장될 때까지 순서대로 백트래킹 수행
    for i in range(n):
        if not visited[i]:
            stack.append(a[i])
            visited[i] = True
            back_tracking(count + 1)
            stack.pop()
            visited[i] = False
```

> permutations 함수를 이용한 풀이 방법
```
from itertools import permutations

# permutations 함수를 이용하여 개수가 n인 순열 저장
perm = list(permutations(a, n))

# 리스트에 있는 값을 차례대로 절댓값 차를 구하고 합
def cal_abs(p):
    result = 0
    for i in range(n - 1):
        result += abs(p[i] - p[i + 1])
    return result

max_val = -1e9
# perm에 저장된 순열 리스트를 하나씩 순회하면서 최댓값 비교
for p in perm:
    max_val = max(max_val, cal_abs(p))

print(max_val)
```