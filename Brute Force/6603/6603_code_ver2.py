def back_tracking(count):
    if count == 6:
        print(*stack)
        return

    for i in range(k):
        if s[i] not in stack and (not stack or s[i] > stack[-1]):
            stack.append(s[i])
            back_tracking(count + 1)
            stack.pop()

while True:
    array = list(map(int, input().split()))
    k = array[0]

    if k == 0:
        break
    else:
        s = array[1:]
        stack = []
        back_tracking(0)
        print()
        