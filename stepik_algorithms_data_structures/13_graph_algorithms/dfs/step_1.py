import sys


def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, visited, i)
        count += 1

print(count)
