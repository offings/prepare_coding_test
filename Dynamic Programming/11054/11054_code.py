n = int(input())
num_list = list(map(int, input().split()))
re_num_list = num_list[::-1]

increase = [1] * n
decrease = [1] * n

for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if re_num_list[i] > re_num_list[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

decrease.reverse()

max_len = 0
for i in range(n):
    if increase[i] + decrease[i] > max_len:
        max_len = increase[i] + decrease[i]
        
print(max_len - 1)


