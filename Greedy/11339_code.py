n = int(input())
people = list(map(int, input().split()))

people.sort()
for i in range(1, n):
    people[i] += people[i - 1]

print(sum(people))