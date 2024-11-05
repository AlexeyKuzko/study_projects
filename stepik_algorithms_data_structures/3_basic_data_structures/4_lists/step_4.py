class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_nodes_with_value(head, val):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        if curr.data == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    if dummy.next:
        return dummy.next
    else:
        return None


def print_list(head):
    if head is None:
        print("None")
    else:
        curr = head
        while curr:
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
        curr.next = Node(data[i])
        curr = curr.next

new_head = delete_nodes_with_value(head, val)
print_list(new_head)
