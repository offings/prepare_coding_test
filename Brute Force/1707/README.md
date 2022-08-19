## 백준 1707 이분 그래프
[문제 링크](https://www.acmicpc.net/problem/1707)

## 문제
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

## 핵심 포인트
```
- 이분 그래프가 되려면 인접한 정점과 그룹이 모두 달라야 한다. - 따라서 인접한 정점의 그룹이 이미 정해져 있다면(visited가 0이 아니라면) 그 그룹은 현재 노드의 그룹과 반드시 달라야 한다.
- 하나라도 이분 그래프를 만족하지 않는다면 출력 후 바로 종료한다.
```

## 핵심 코드
```
def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1

    while queue:
        x = queue.popleft()
        color = visited[x]

        for c in graph[x]:
            # 연결되어 있는 노드가 방문하지 않은 노드라면 현재 노드의 그룹과 다른 그룹으로 배정
            if not visited[c]:
                if color == 1:
                    visited[c] = 2
                else:
                    visited[c] = 1

            # 연결되어 있는 노드가 방문한 노드라면 현재 노드의 그룹과 같은지 확인
            # 같은 경우는 NO를 출력하고 False 반환
            # 현재 color가 1일 경우
            elif visited[c] == 1 and color == visited[c]:
                print('NO')
                return False

            # 현재 color가 2일 경우
            elif visited[c] == 2 and color == visited[c]:
                print('NO')
                return False

    # 연결 그래프가 아닐 경우를 대비하여 전체 노드 탐색
    for i in range(1, v + 1):
        if not visited[i]:
            is_binary = bfs(i)
            # 하나라도 이분 그래프가 아닌 것이 발견되었다면 즉시 종료
            if not is_binary:
                break

    # 이분 그래프 조건을 만족한다면 YES 출력
    if is_binary:
        print('YES')

```