import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**25)


def dfs(graph, visited, path, node):
    visited[node] = True
    path.append(node)
    for neighbor in graph[node]:
        if visited[neighbor]:
            if neighbor in path:
                index = path.index(neighbor)
                return path[index:]
        else:
            cycle = dfs(graph, visited, path, neighbor)
            if cycle:
                return cycle
    path.pop()
    return None


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
            if not visited[i]:
                cycle = dfs(graph, visited, [], i)
                if cycle:
                    print(len(cycle))
                    print(*cycle)
                    break
        else:
            print(-1)


thread = threading.Thread(target=solve)
thread.start()
thread.join()
