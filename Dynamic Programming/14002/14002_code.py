n = int(input())
num_list = list(map(int, input().split()))
max_cnt = [1] * n

for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            max_cnt[i] = max(max_cnt[i], max_cnt[j] + 1)

max_val = max(max_cnt)
print(max_val)

max_idx = max_cnt.index(max_val)
max_list = []
while max_val > 0:
    if max_cnt[max_idx] == max_val:
        max_list.append(num_list[max_idx])
        max_val -= 1
    max_idx -= 1

max_list.reverse()
print(*max_list)

