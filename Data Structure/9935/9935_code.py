import sys
input = sys.stdin.readline

total_str = input().strip()
bomb = input().strip()
len_bomb = len(bomb)

stack = []
for i in range(len(total_str)):
    stack.append(total_str[i])
    if ''.join(stack[-len_bomb:]) == bomb:
        # del stack[-len_bomb:]
        for j in range(len_bomb):
            stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))