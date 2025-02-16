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
