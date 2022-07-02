n = int(input())
stars = [[' '] * (2 * n - 1) for _ in range(n)]

def divide_star(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = '*'
        for k in range(-2, 3):
            stars[i + 2][j + k] = '*'

    else:
        new_size = size // 2
        divide_star(i, j, new_size)
        divide_star(i + new_size, j - new_size, new_size)
        divide_star(i + new_size, j + new_size, new_size)

divide_star(0, n - 1, n)
for star in stars:
    print(''.join(star))
