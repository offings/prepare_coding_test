## 백준 2252 줄 세우기
[문제 링크](https://www.acmicpc.net/problem/2252)

## 문제
N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

## 핵심 포인트
```
- 위상 정렬(Topological Sort)은 방향 그래프에서 간선의 방향을 위배하지 않으면서 순서를 찾는 방법이다.
- 모든 정점의 진입 차수를 계산하여 진입 차수가 0인 정점을 큐에 삽입하면서 알고리즘을 수행한다.
```

## 핵심 코드
```
for _ in range(m):
    a, b = map(int, input().split())
    # b는 a와 간선으로 연결되어 있으므로 진입차수 증가
    in_degree[b] += 1
    student[a].append(b)

for i in range(1, n + 1):
    # 진입차수가 0인 정점을 큐에 삽입
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    answer.append(x)
    # 큐에서 뺀 정점과 연결된 모든 정점의 진입차수를 1씩 감소
    for next in student[x]:
        in_degree[next] -= 1
        # 정점의 진입차수가 0이라면 큐에 삽입
        if in_degree[next] == 0:
            queue.append(next)
```
