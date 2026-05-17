"""Solution for Stepik course solutions: Algorithms Data Structures / 3 Basic Data Structures / 6 Queue / Step 6."""

n = int(input())
queue = []

for _ in range(n):
    command = input().split()
    if command[0] == "ADD":
        queue.append(command[1])
    elif command[0] == "NEXT":
        if not queue:
            print("Queue is empty")
        else:
            queue.pop(0)
    elif command[0] == "COUNT":
        print(len(queue))
