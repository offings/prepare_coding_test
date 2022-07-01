from collections import deque
   
n, k = map(int, input().split())
max_val = 1000001
dist = [-1] * max_val

def bfs(s):
    queue = deque()
    queue.append(s)
    dist[s] = 0

    while queue:
        node = queue.popleft()
        if node == k:
            print(dist[node])
            break

        if 0 <= node * 2 < max_val and dist[node * 2] == -1:
            queue.appendleft(node * 2)
            dist[node * 2] = dist[node]

        for next_node in [node - 1, node + 1]:
            if 0 <= next_node < max_val and dist[next_node] == -1:
                queue.append(next_node)
                dist[next_node] = dist[node] + 1

bfs(n)

