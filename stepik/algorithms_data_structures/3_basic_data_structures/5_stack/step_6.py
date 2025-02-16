stack = []

while True:
    command = input().split()
    if command[0] == "push":
        stack.append(int(command[1]))
        print("ok")
    elif command[0] == "pop":
        if not stack:
            print("error")
        else:
            print(stack.pop())
    elif command[0] == "back":
        if not stack:
            print("error")
        else:
            print(stack[-1])
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "clear":
        stack = []
        print("ok")
    elif command[0] == "exit":
        print("bye")
        break
