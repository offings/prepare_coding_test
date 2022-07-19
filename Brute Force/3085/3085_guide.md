## 백준 3085 사탕 게임
[문제 링크](https://www.acmicpc.net/problem/3085)

## 문제
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

## 핵심 포인트
```
- 1초에 처리할 수 있는 양은 1억이므로 N = 50일 때, O(N ** 4)는 처리 가능하다.
- 좌우로 값이 다를 때 바꾸는 경우와 상하로 값이 다를 때 바꾸는 경우를 모두 고려하여 최대 개수를 구한다.
- 인접한 두 칸의 값을 바꾸고 최대 개수를 구한 다음 다시 원래 값이 되도록 값을 한 번 더 교환한다.
- find_max() 함수에서 한 행(열)에 최대 개수가 나왔을 때 값을 저장해야 하므로 temp 값을 바꾸고 바로 값을 비교한다.
```

## 핵심 코드
```
def find_max():
    answer = 1
    for i in range(n):
        temp = 1
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                temp += 1
            else:
                temp = 1
            answer = max(temp, answer)

    for i in range(n):
        temp = 1
        for j in range(n - 1):
            if board[j][i] == board[j + 1][i]:
                temp += 1
            else:
                temp = 1
            answer = max(temp, answer)

    return answer
```
