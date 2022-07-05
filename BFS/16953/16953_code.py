from collections import deque

def bfs(s):
    queue = deque()
    queue.append([s, 1])

    while queue:
        num, cost = queue.popleft()
        if num == b:
            print(cost)
            return
        
        for next_num in [num * 2, num * 10 + 1]:
            if next_num <= b:
                queue.append([next_num, cost + 1])
    
    print(-1)

a, b = map(int, input().split())
bfs(a)
