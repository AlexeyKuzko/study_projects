import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**25)


def dfs(graph, visited, path, node, target):
    visited[node] = True
    path.append(node)
    if node == target:
        return True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(graph, visited, path, neighbor, target):
                return True
    path.pop()
    return False


def solve():
    t = int(input())
    for _ in range(t):
        n, m, s, t = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)

        visited = [False] * (n + 1)
        path = []
        if dfs(graph, visited, path, s, t):
            print(*path)
        else:
            print(-1)


thread = threading.Thread(target=solve)
thread.start()
thread.join()
