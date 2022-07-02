# N과 M (2)
def back_tracking():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
    
    else:
        for num in range(1, n + 1):
            if not stack or (num not in stack and stack[-1] < num):
                stack.append(num)
                back_tracking()
                stack.pop()

n, m = map(int, input().split())
stack = []
back_tracking()