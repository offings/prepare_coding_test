n, s = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

def back_tracking(idx, total):
    global count
    if idx == n:
        if total == s:
            count += 1
        return

    back_tracking(idx + 1, total + num_list[idx])   
    back_tracking(idx + 1, total)

back_tracking(0, 0)

if s == 0:
    print(count - 1)
else:
    print(count)