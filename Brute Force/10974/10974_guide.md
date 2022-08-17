## 백준 10974 모든 순열
[문제 링크](https://www.acmicpc.net/problem/10974)

## 문제
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

## 핵심 포인트
```
- N이 8 이하이므로 기본 백트래킹 원리를 적용해도 시간 초과가 발생하지 않는다. 
```

## 핵심 코드
```
def back_tracking(count):
    # stack에 있는 수가 n개와 같다면 stack 값 출력
    if count == n: 
        print(*stack)
        return

    # 모든 수가 stack에 포함될 때까지 반복
    for i in range(1, n + 1):
        # stack에 있는 수와 겹치지 않는다면
        if i not in stack:
            # stack에 삽입하고 count 증가
            stack.append(i)
            back_tracking(count + 1)
            # stack에 있는 값을 출력했다면 마지막 값 pop
            stack.pop()
```
