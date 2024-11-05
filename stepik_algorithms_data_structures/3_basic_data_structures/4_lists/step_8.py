class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def remove_all_nodes_with_value(head, val):
    if head is None:
        return None

    while head is not None and head.data == val:
        head = head.next
        if head is not None:
            head.prev = None

    curr = head
    while curr is not None:
        if curr.data == val:
            if curr.next is not None:
                curr.next.prev = curr.prev
            if curr.prev is not None:
                curr.prev.next = curr.next
        curr = curr.next

    return head

def print_list(head):
    if head is None:
        print("None")
        return

    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

n = int(input())
data = list(map(int, input().split()))
val = int(input())

head = None
if n > 0:
    head = Node(data[0])
    curr = head
    for i in range(1, n):
        new_node = Node(data[i])
        curr.next = new_node
        new_node.prev = curr
        curr = new_node

head = remove_all_nodes_with_value(head, val)
print_list(head)