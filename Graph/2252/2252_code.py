from collections import deque
n, m = map(int, input().split())

in_degree = [0] * (n + 1)
student = [[] for _ in range(n + 1)]
queue = deque()
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    in_degree[b] += 1
    student[a].append(b)

for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    answer.append(x)
    for next in student[x]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            queue.append(next)

print(*answer)