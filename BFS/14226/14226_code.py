from collections import deque
s = int(input())

queue = deque()
queue.append((1, 0))
dist = dict()
dist[(1, 0)] = 0

while queue:
    screen, clip = queue.popleft()

    if screen == s:
        print(dist[screen, clip])
        break

    if (screen, screen) not in dist.keys():
        queue.append((screen, screen))
        dist[(screen, screen)] = dist[(screen, clip)] + 1

    if (screen + clip, clip) not in dist.keys():
        queue.append((screen + clip, clip))
        dist[(screen + clip, clip)] = dist[(screen, clip)] + 1

    if screen - 1 >= 0 and (screen - 1, clip) not in dist.keys():
        queue.append((screen - 1, clip))
        dist[(screen - 1, clip)] = dist[(screen, clip)] + 1
