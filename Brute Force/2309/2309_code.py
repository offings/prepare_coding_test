from itertools import combinations
dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
dwarf.sort()

d_list = list(combinations(dwarf, 7))

for d in d_list:
    if sum(d) == 100:
        print('\n'.join(map(str, d)))
        break


