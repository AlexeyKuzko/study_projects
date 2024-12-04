import sys
from collections import deque


def bfs(graph, s, t):
    queue = deque([(s, 0)])
    visited = set()
    while queue:
        node, distance = queue.popleft()
        if node == t:
            return distance
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            queue.append((neighbor, distance + 1))
    return -1


def solve():
    n, m, s, t = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
    print(bfs(graph, s, t))


for _ in range(int(sys.stdin.readline())):
    solve()
