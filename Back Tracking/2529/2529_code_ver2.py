k = int(input())
sign = list(input().split())
min_val = ''
max_val = ''
visited = [False] * 10

def is_possible(left, right, sid):
    if sign[sid] == '<':
        return left < right
    else:
        return left > right

def back_tracking(count, s):
    global min_val, max_val
    if len(s) == k + 1:
        if not len(min_val):
            min_val = s
        else:
            max_val = s
        return

    for i in range(10):
        if not visited[i]:
            if count == 0 or is_possible(s[-1], str(i), count - 1):
                visited[i] = True
                back_tracking(count + 1, s + str(i))
                visited[i] = False

back_tracking(0, '')
print(max_val)
print(min_val)