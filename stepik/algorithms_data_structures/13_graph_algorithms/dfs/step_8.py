import sys
from collections import deque


def solve():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[b].append(a)
        in_degree[a] += 1

    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    days = 0
    while queue:
        days += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    print(days)


solve()
