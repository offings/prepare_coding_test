k = int(input())
sign = list(input().split())

stack = []
min_val = int(1e10)
max_val = 0

def back_tracking(number, sid):
    global min_val, max_val
    if sid == k:
        stack.append(number)
        min_val = min(min_val, int(''.join(map(str, stack))))
        max_val = max(max_val, int(''.join(map(str, stack))))
        return

    stack.append(number)
    s = sign[sid]

    if s == '<':
        for i in range(number + 1, 10):
            if i not in stack:
                back_tracking(i, sid + 1)
                stack.pop()

    elif s == '>':
        for i in range(number):
            if i not in stack:
                back_tracking(i, sid + 1)
                stack.pop()

for i in range(10):
    back_tracking(i, 0)
    stack.pop()

if len(str(max_val)) < k + 1:
    max_val = '0' + str(max_val)
if len(str(min_val)) < k + 1:
    min_val = '0' + str(min_val) 

print(max_val)
print(min_val)