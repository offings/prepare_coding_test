from collections import deque
def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1

    while queue:
        x = queue.popleft()
        color = visited[x]
        
        for c in graph[x]:
            if not visited[c]:
                queue.append(c)
                if color == 1:
                    visited[c] = 2
                else:
                    visited[c] = 1

            elif visited[c] == 1 and color == visited[c]:
                print('NO')
                return False
                
            elif visited[c] == 2 and color == visited[c]:
                print('NO')
                return False

    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for _ in range(e):
        u1, u2 = map(int, input().split())
        graph[u1].append(u2)
        graph[u2].append(u1)

    for i in range(1, v + 1):
        if not visited[i]:
            is_binary = bfs(i)   
            if not is_binary:
                break

    if is_binary:
        print('YES') 

