## 백준 4803 트리
[문제 링크](https://www.acmicpc.net/problem/4803)

## 문제
그래프는 정점과 간선으로 이루어져 있다. 두 정점 사이에 경로가 있다면, 두 정점은 연결되어 있다고 한다. 연결 요소는 모든 정점이 서로 연결되어 있는 정점의 부분집합이다. 그래프는 하나 또는 그 이상의 연결 요소로 이루어져 있다. 트리는 사이클이 없는 요소이다. 트리에는 여러 성질이 있다. 예를 들어, 트리는 정점이 n개, 간선이 n-1개 있다. 또, 임의의 두 정점에 대해서 경로가 유일하다. 그래프가 주어졌을 때, 트리의 개수를 세는 프로그램을 작성하시오.

## 핵심 포인트
```
- 정점이 하나라도 트리가 될 수 있다.
- 트리는 사이클(cycle)이 없어야 한다.
```

## 핵심 코드
> DFS를 이용한 트리 판별
```
def dfs(prev, v):
    visited[v] = True

    for c in graph[v]:
        if prev == c:
            continue
        if visited[c]: # 사이클이 존재
            return False
        if not dfs(v, c):
            return False

    return True

for i in range(1, n + 1):
    if not visited[i]:
        if dfs(0, v):
            n_tree += 1
```
> Union-Find를 활용한 트리 판별
```
def find(v):
    if v != parents[v]:
        parents[v] = find(parents[v])
    return parents[v]

def union(u, v):
    u = find(u); v = find(v)
    if u < v:
        parents[v] = u
    else:
        parents[u] = v

u, v = map(int, input().split())
find_u = find(u); find_v = find(v)

if find_u != find_v: # 사이클이 없는 경우
    union(u, v) 
else: # 사이클이 있을 경우
    cycle.add(u)
```
