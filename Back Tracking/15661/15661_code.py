import sys
input = sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
visited = [False] * n
min_val = int(1e6)

def cal_score():
    global min_val
    start, link = 0, 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if visited[i] and visited[j]:
                start += s[i][j] + s[j][i]
            elif not visited[i] and not visited[j]:
                link += s[i][j] + s[j][i]

    min_val = min(min_val, abs(start - link))
    
def back_tracking(number):
    if number == n:
        cal_score()
        return

    visited[number] = True
    back_tracking(number + 1)
    visited[number] = False
    back_tracking(number + 1)

back_tracking(0)
print(min_val)
    