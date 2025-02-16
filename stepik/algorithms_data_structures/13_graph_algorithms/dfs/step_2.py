import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**25)


def dfs(graph, visited, node, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor, component)


def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            dfs(graph, visited, i, component)
            components.append(component)

    print(len(components))
    for component in components:
        print(len(component), *sorted(component))


thread = threading.Thread(target=solve)
thread.start()
thread.join()
