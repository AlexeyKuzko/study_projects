import sys
from collections import deque


def bfs(maze, n):
    directions = [(0, 1, "r"), (0, -1, "l"), (1, 0, "d"), (-1, 0, "u")]
    queue = deque([(0, 0, "")])
    visited = set((0, 0))
    while queue:
        x, y, path = queue.popleft()
        if x == n - 1 and y == n - 1:
            return len(path), path
        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy
            if (
                (0 <= nx < n)
                and (0 <= ny < n)
                and maze[nx][ny] == "."
                and (nx, ny) not in visited
            ):
                queue.append((nx, ny, path + direction))
                visited.add((nx, ny))
    return -1, ""


def solve():
    n = int(sys.stdin.readline())
    maze = [list(sys.stdin.readline().strip()) for _ in range(n)]
    steps, path = bfs(maze, n)
    print(steps)
    if steps != -1:
        print(path)


t = 1
for _ in range(t):
    solve()
