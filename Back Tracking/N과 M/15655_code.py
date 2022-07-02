# N과 M (6)
def back_tracking():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
    else:
        for num in num_list:
            if not stack or (num not in stack and stack[-1] < num):
                stack.append(num)
                back_tracking()
                stack.pop()

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
stack = []
back_tracking()