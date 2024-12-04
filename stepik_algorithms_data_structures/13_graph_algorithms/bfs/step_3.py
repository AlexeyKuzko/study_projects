import sys
from collections import deque


def bfs(graph, s, k):
    queue = deque([(s, 0)])
    visited = set()
    count = 0
    while queue:
        node, distance = queue.popleft()
        if node in visited or distance > k:
            continue
        visited.add(node)
        if node != s:
            count += 1
        for neighbor in graph[node]:
            queue.append((neighbor, distance + 1))
    return count


def solve():
    n, m, s, k = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
    print(bfs(graph, s, k))


t = 1
for _ in range(t):
    solve()
