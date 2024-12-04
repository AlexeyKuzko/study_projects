import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**25)


def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if visited[neighbor]:
            return False
        if not dfs(graph, visited, neighbor):
            return False
    visited[node] = False
    return True


def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)

        visited = [False] * (n + 1)
        for i in range(1, n + 1):
            if not dfs(graph, visited, i):
                print("No")
                break
        else:
            print("Yes")


thread = threading.Thread(target=solve)
thread.start()
thread.join()
