## 백준 2638 치즈
[문제 링크](https://www.acmicpc.net/problem/2638)

## 문제
N×M의 모눈종이 위에 아주 얇은 치즈가 <그림 1>과 같이 표시되어 있다. 단, N 은 세로 격자의 수이고, M 은 가로 격자의 수이다. 이 치즈는 냉동 보관을 해야만 하는데 실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다. 그런데 이러한 모눈종이 모양의 치즈에서 각 치즈 격자(작 은 정사각형 모양)의 4변 중에서 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다. 따라서 아래 <그림 1> 모양과 같은 치즈(회색으로 표시된 부분)라면 C로 표시된 모든 치즈 격자는 한 시간 후에 사라진다.  
![그림 1](./%EA%B7%B8%EB%A6%BC1.jpg)

<그림 2>와 같이 치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정한다. 그러므 로 이 공간에 접촉한 치즈 격자는 녹지 않고 C로 표시된 치즈 격자만 사라진다. 그러나 한 시간 후, 이 공간으로 외부공기가 유입되면 <그림 3>에서와 같이 C로 표시된 치즈 격자들이 사라지게 된다.
![그림 2](./%EA%B7%B8%EB%A6%BC2.jpg)
![그림 3](./%EA%B7%B8%EB%A6%BC%203.jpg)

## 핵심 포인트
```
- 0에서 1로 갈 수 있는 경우가 2개 이상일 경우 치즈는 녹는다.
- BFS를 진행하면서 입력 받은 배열의 값이 1이면 값을 더해주고, 0이면 방문 처리와 queue 삽입을 해준다.
- 입력 받은 배열의 값이 3 이상일 경우 4변 중 2변 이상 접한 것이므로, 다음 BFS 전 배열의 값을 0으로 업데이트한다.
```

## 핵심 코드
```
def bfs():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    # 치즈가 실온에 접촉한 경우
                    if paper[nx][ny] >= 1:
                        # 1면에 접촉했으므로 값 증가
                        paper[nx][ny] += 1
                    # 실온 공기인 경우
                    else:
                        visited[nx][ny] = True
                        queue.append([nx, ny])

time = 0
while True:
    visited = [[False] * m for _ in range(n)]
    flag = 0
    bfs()

    for i in range(n):
        for j in range(m):
            # 치즈가 실온에 두 면 이상 접촉
            if paper[i][j] >= 3:
                # 치즈가 녹았으므로 0으로 설정
                paper[i][j] = 0
                # 시간 설정을 위해 체크 표시
                flag = 1
            # 치즈가 실온 한 면에 접촉
            elif paper[i][j] == 2:
                # 상하지 않으므로 원래 값 유지
                paper[i][j] = 1

    if flag:
        time += 1
    else:
        break
```
