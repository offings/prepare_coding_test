dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
dwarf.sort()

not_dwarf = []
for i in range(9):
    for j in range(i + 1, 9):
        if (sum(dwarf) - dwarf[i] - dwarf[j]) == 100:
            not_dwarf.append(dwarf[i])
            not_dwarf.append(dwarf[j])
            break

dwarf.remove(not_dwarf[0])
dwarf.remove(not_dwarf[1])

print('\n'.join(map(str, dwarf)))
