import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**25)


def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)


def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (n + 1)
        components = 0
        for i in range(1, n + 1):
            if not visited[i]:
                dfs(graph, visited, i)
                components += 1

        if components == 1 and m == n - 1:
            print("YES")
        else:
            print("NO")


thread = threading.Thread(target=solve)
thread.start()
thread.join()
