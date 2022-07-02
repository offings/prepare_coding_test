# N과 M (9)
n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
stack = []
visited = [False] * n

def back_tracking():
    if len(stack) == m:
        print(*stack)
    else:
        overlap = 0
        for i in range(n):
            if not visited[i] and (overlap != num_list[i]):
                visited[i] = True
                stack.append(num_list[i])
                overlap = num_list[i]
                back_tracking()
                visited[i] = False
                stack.pop()
                
back_tracking()
