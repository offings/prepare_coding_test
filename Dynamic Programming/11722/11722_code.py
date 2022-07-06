n = int(input())
num_list = list(map(int, input().split()))
max_cnt = [1] * n

for i in range(n):
    for j in range(i):
        if num_list[i] < num_list[j]:
            max_cnt[i] = max(max_cnt[i], max_cnt[j] + 1)

print(max_cnt)
print(max(max_cnt))