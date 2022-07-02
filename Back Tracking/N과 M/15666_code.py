# N과 M (12)
n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
stack = []

def back_tracking():
    if len(stack) == m:
        print(*stack)
    else:
        overlap = 0
        for i in range(n):
            if overlap != num_list[i] and (not stack or stack[-1] <= num_list[i]):
                stack.append(num_list[i])
                overlap = num_list[i]
                back_tracking()
                stack.pop()

back_tracking()