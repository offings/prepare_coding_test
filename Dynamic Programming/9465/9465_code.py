import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    
    for i in range(1, n):
        if i == 1:
            stickers[0][1] += stickers[1][0]
            stickers[1][1] += stickers[0][0]

        else:
            stickers[0][i] += max(stickers[1][i - 1], stickers[1][i - 2])
            stickers[1][i] += max(stickers[0][i - 1], stickers[0][i - 2])

    print(max(stickers[0][-1], stickers[1][-1]))
