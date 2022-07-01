import sys
input = sys.stdin.readline

n, k = map(int, input().split())

knapsack = [[0] * (k + 1) for _ in range(n + 1)]
for v in range(1, n + 1):
    weight, value = map(int, input().split())
    
    for w in range(1, k + 1):
        if w < weight:
            knapsack[v][w] = knapsack[v-1][w]
        else:
            knapsack[v][w] = max(value + knapsack[v-1][w - weight], knapsack[v-1][w])

print(knapsack[n][k])
