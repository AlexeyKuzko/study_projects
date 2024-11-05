class Queue:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)
        print("ok")

    def pop(self):
        if self.items:
            print(self.items.pop(0))
        else:
            print("error")

    def front(self):
        if self.items:
            print(self.items[0])
        else:
            print("error")

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items = []
        print("ok")

    def exit(self):
        print("bye")


# Чтение команд и выполнение
queue = Queue()

while True:
    command = input().strip()
    if command.startswith("push"):
        _, n = command.split()
        queue.push(int(n))
    elif command == "pop":
        queue.pop()
    elif command == "front":
        queue.front()
    elif command == "size":
        queue.size()
    elif command == "clear":
        queue.clear()
    elif command == "exit":
        queue.exit()
        break
