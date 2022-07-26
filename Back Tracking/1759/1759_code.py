import sys
input = sys.stdin.readline

l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()
pw = []

def is_possible():
    cur_vo, cur_cnt = 0, 0
    for i in range(l):
        if pw[i] in ['a', 'e', 'i', 'o', 'u']:
            cur_vo += 1
        else:
            cur_cnt += 1

    if cur_vo >= 1 and cur_cnt >= 2:
        print(''.join(pw))

def back_tracking(count):
    if count == l:
        is_possible()
        return

    for a in alpha:
        if a not in pw:
            if len(pw) == 0 or a > pw[-1]:
                pw.append(a)
                back_tracking(count + 1)
                pw.pop()

back_tracking(0)