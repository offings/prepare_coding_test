## 백준 4375 1
[문제 링크](https://www.acmicpc.net/problem/4375)

## 문제
2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

## 핵심 포인트
```
- 입력의 개수가 주어지지 않은 경우 try - except 구문을 활용하여 입력 받는다.
- 1로만 이루어진 n의 배수의 의미를 파악한다. ex) 111이라는 수는 1로만 이루어져있고 3의 배수이다.
```

## 핵심 코드
```
def find_digit(num):
    one = 1
    while True:
        # 1로 이루어진 수이고 num의 배수일 때 
        if one % num == 0:
            return len(str(one))
        # num의 배수가 아니라면 다음으로 큰 1로 이루어진 수 탐색
        else:
            one = one * 10 + 1

while True:
    try:
        num = int(input())
        print(find_digit(num))
    except:
        break
```