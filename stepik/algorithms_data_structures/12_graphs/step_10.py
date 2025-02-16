import sys

n, m = map(int, input().split())
edges = {}
for _ in range(m):
    a, b = map(int, input().split())
    if a not in edges:
        edges[a] = set()
    if b not in edges:
        edges[b] = set()
    edges[a].add(b)
    edges[b].add(a)

count = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if i in edges and j in edges[i]:
            for k in range(j + 1, n + 1):
                if j in edges and k in edges[j] and k in edges[i]:
                    count += 1

print(count)
