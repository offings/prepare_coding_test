n = input()
num_list = [0] * 10

for each_n in n:
    each_n = int(each_n)
    num_list[each_n] += 1

if num_list[9] != num_list[6]:
    total = num_list[9] + num_list[6]
    half = (num_list[9] + num_list[6]) // 2
    num_list[9] = half
    num_list[6] = total - half

print(max(num_list))


