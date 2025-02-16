import sys

n, m, q = map(int, input().split())
edges = {}
for _ in range(m):
    a, b = map(int, input().split())
    if a not in edges:
        edges[a] = set()
    if b not in edges:
        edges[b] = set()
    edges[a].add(b)
    edges[b].add(a)

result = []
for _ in range(q):
    _, x, y = input().split()
    x, y = int(x), int(y)
    if x in edges and y in edges[x]:
        result.append("1")
    else:
        result.append("0")

print("".join(result))
