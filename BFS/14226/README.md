## 백준 14226 이모티콘
[문제 링크](https://www.acmicpc.net/problem/14226)

## 문제
영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.

영선이는 이미 화면에 이모티콘 1개를 입력했다. 이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.

화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
화면에 있는 이모티콘 중 하나를 삭제한다.
모든 연산은 1초가 걸린다. 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다. 또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다. 화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.

영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

## 핵심 포인트
```
- 일반 BFS와는 달리 queue에 (화면 스티커 개수, 클립보드 스티커 개수)를 함께 저장한다.
- dist 배열 대신 딕셔너리를 사용하여 (화면 스티커 개수, 클립보드 스티커 개수)의 중복을 확인하고 값을 업데이트한다.
- 화면에 있는 스티커가 음수는 될 수 없으므로 삭제 시 화면의 스티커가 음수가 되면 queue 삽입을 제한한다.
```

## 핵심 코드
```
queue = deque()
# queue에는 (화면 스티커 개수, 클립보드 스티커 개수) 순으로 저장
queue.append((1, 0))
# 방문 표시 확인(중복 확인)을 위해 딕셔너리 선언
dist = dict()
dist[(1, 0)] = 0

while queue:
    # queue에 가장 앞에 있는 값을 pop
    screen, clip = queue.popleft()

    # 현재 화면에 있는 값이 주어진 s와 같으면 시간의 최솟값을 출력하고 반복문 탈출
    if screen == s:
        print(dist[(screen, clip)])
        break

    # 화면에 있는 스티커를 모두 복사한 경우
    # 현재 화면에 있는 스티커 개수와 복사한 스티커 개수가 이전에 삽입되지 않았던 조합이라면 queue에 삽입 후 최솟값 업데이트
    if (screen, screen) not in dist.keys():
        queue.append((screen, screen))
        dist[(screen, screen)] = dist[(screen, dist)] + 1

    # 클립보드에 저장된 이모티콘을 화면에 붙여넣기한 경우
    if (screen + clip, clip) not in dist.keys():
        queue.append((screen + clip, clip))
        dist[(screen + clip, clip)] = dist[(screen, dist)] + 1

    # 화면에 있는 이모티콘을 하나 삭제한 경우
    # 화면에 있는 이모티콘이 음수가 될 수는 없으므로 screen - 1이 0보다 커야 한다는 조건 추가
    if screen - 1 >= 0 and (screen - 1, clip) not in dist.keys():
        queue.append((screen - 1, clip))
        dist[(screen - 1, clip)] = dist[(screen, dist)] + 1
```
