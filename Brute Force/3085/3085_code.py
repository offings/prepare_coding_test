import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(input().strip()))

def find_max():
    answer = 1
    for i in range(n):
        temp = 1
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                temp += 1
            else:
                temp = 1
            answer = max(temp, answer)

    for i in range(n):
        temp = 1
        for j in range(n - 1):
            if board[j][i] == board[j + 1][i]:
                temp += 1
            else:
                temp = 1
            answer = max(temp, answer)

    return answer

max_candy = 1
for i in range(n):
    for j in range(n - 1):
        if board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            max_candy = max(max_candy, find_max())
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

for i in range(n):
    for j in range(n - 1):
        if board[j][i] != board[j + 1][i]:
            board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
            max_candy = max(max_candy, find_max())
            board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]

print(max_candy)