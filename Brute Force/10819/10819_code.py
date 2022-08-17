n = int(input())
a = list(map(int, input().split()))

stack = []
visited = [False] * n
max_val = -1e9
def cal_abs():
    result = 0
    for i in range(n - 1):
        result += abs(stack[i] - stack[i + 1])
    return result

def back_tracking(count):
    global max_val
    if count == n:
        max_val = max(max_val, cal_abs())
        return

    for i in range(n):
        if not visited[i]:
            stack.append(a[i])
            visited[i] = True
            back_tracking(count + 1)
            stack.pop()
            visited[i] = False

back_tracking(0)
print(max_val)