import bisect

n = int(input())
num_list = list(map(int, input().split()))
idx_list = [0]
max_list = [num_list[0]]

for i in range(1, n):
    if num_list[i] > max_list[-1]:
        idx_list.append(len(max_list))
        max_list.append(num_list[i])
    else:
        idx = bisect.bisect_left(max_list, num_list[i])
        max_list[idx] = num_list[i]
        idx_list.append(idx)

max_val = len(max_list) - 1
print(max_val + 1)

max_idx = idx_list.index(max_val)
result_list = []

while max_val >= 0:
    if idx_list[max_idx] == max_val:
        result_list.append(num_list[max_idx])
        max_val -= 1
    max_idx -= 1

result_list.reverse()
print(*result_list)
