n, m = map(int, input().split())
p = []
for _ in range(n):
    p.append(list(map(int, input())))

answer = 0
def bit_masking():
    global answer
    for i in range(1 << n * m):
        total = 0

        for r in range(n):
            row_sum = 0
            for c in range(m):
                idx = r * m + c
                if i & (1 << idx) != 0:
                    row_sum = row_sum * 10 + p[r][c]
                else:
                    total += row_sum
                    row_sum = 0
            total += row_sum

        for c in range(m):
            col_sum = 0
            for r in range(n):
                idx = r * m + c
                if i & (1 << idx) == 0:
                    col_sum = col_sum * 10 + p[r][c]
                else:
                    total += col_sum
                    col_sum = 0
            total += col_sum

        answer = max(answer, total)

bit_masking()
print(answer)