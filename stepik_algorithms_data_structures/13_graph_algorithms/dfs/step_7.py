import sys
from collections import deque


def bfs(graph, colors, start):
    queue = deque([start])
    colors[start] = 1
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if colors[neighbor] == colors[node]:
                return False
            if colors[neighbor] == 0:
                colors[neighbor] = 3 - colors[node]
                queue.append(neighbor)
    return True


def solve():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    colors = [0] * (n + 1)
    for i in range(1, n + 1):
        if colors[i] == 0:
            if not bfs(graph, colors, i):
                print(-1)
                return
    print(*colors[1:])


solve()
