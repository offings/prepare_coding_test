n = int(input())
num_list = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if num_list[i] > num_list[i - 1]:
        for j in range(n - 1, 0, -1):
            if num_list[j] > num_list[i - 1]:
                num_list[j], num_list[i - 1] = num_list[i - 1], num_list[j]
                num_list = num_list[:i] + sorted(num_list[i:])
                print(*num_list)
                exit(0)

print(-1)