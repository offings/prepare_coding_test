import sys
input = sys.stdin.readline

def find(v):
    if v != parent[v]:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    u = find(u)
    v = find(v)

    if u < v:
        parent[v] = u
    else:
        parent[u] = v

n_test = 0
while True:
    n_test += 1
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    cycle = set()

    for _ in range(m):
        u, v = map(int, input().split())
        find_u = find(u)
        find_v = find(v)
        if find_u != find_v:
            union(u, v)
        else:
            cycle.add(u)

    for i in range(n + 1):
        find(i)

    group = set()
    for cycle_vertex in cycle:
        group.add(parent[cycle_vertex])

    n_tree = 0
    for i in range(1, n + 1):
        if parent[i] in group:
            continue
        n_tree += 1
        group.add(parent[i])

    if n_tree > 1:
        print(f'Case {n_test}: A forest of {n_tree} trees.')
    elif n_tree == 1:
        print(f'Case {n_test}: There is one tree.')
    else:
        print(f'Case {n_test}: No trees.')
