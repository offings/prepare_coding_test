## 백준 13023 ABCDE
[문제 링크](https://www.acmicpc.net/problem/13023)

## 문제
BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.
위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

## 핵심 포인트
```
- 위와 같은 친구 관계는 depth가 4일 때, 즉 dfs로 호출할 수 있는 재귀 횟수가 4 이상일 때이다.
- 본 코드는 친구의 수를 기준으로 depth를 정했기 때문에 depth가 5일 때 본 조건을 만족한다.
- 시작점은 0부터 n-1까지 다르게 하여 가능한 전체 dfs 경로 중 하나라도 본 조건을 만족하면 1 출력 후 종료한다.
```

## 핵심 코드
```
def dfs(x, depth):
    # dfs 함수로 들어왔다면 방문 표시
    visited[x] = True

    # 연결된 친구 수가 5라면 1 출력 후 종료
    if depth == 5:
        print(1)
        exit()

    # 현재 노드에서 연결된 친구로 방문할 수 있으면 방문 후 depth 증가
    for c in graph[x]:
        if not visited[c]:
            visited[c] = True
            dfs(c, depth + 1)
            # 호출이 되었다면 다시 방문 표시 해제
            visited[c] = False

# 시작점을 0에서부터 n-1로 변경하여 전체 경우 모두 탐색
for i in range(n):
    dfs(i, 1)
    visited[i] = False

# 연결된 친구 수가 모두 5 미만이라면 0 출력
print(0)
```