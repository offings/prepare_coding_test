n = int(input())

stack = []
def back_tracking(count):
    if count == n:
        print(*stack)
        return

    for i in range(1, n + 1):
        if i not in stack:
            stack.append(i)
            back_tracking(count + 1)
            stack.pop()

back_tracking(0)