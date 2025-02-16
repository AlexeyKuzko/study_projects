import sys
from collections import deque


def bfs(graph, n):
    queue = deque([(1, 0)])
    visited = set()
    distances = [-1] * (n + 1)
    distances[1] = 0
    while queue:
        node, distance = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distance + 1
                queue.append((neighbor, distance + 1))
    return distances[1:]


def solve():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[b].append(a)
    print(*bfs(graph, n))


t = int(sys.stdin.readline())
for _ in range(t):
    solve()
