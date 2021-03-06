## 백준 1932 정수삼각형
[문제 링크](https://www.acmicpc.net/problem/1932)

## 문제
맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

## 핵심 포인트
```
- 각 층의 처음과 끝은 바로 위에 위치한 값을 현재 값과 더한다.
- 나머지는 윗 층의 대각선에 위치한 두 값 중 더 큰 값을 현재 값과 더한다.
```

## 핵심 코드
```
for i in range(2, n + 1):
    for j in range(i):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == i - 1:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
```
