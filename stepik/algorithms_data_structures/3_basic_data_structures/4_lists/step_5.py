class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle_element(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr.data


n = int(input())
data = list(map(int, input().split()))

head = None
if n > 0:
    head = Node(data[0])
    curr = head
    for i in range(1, n):
        curr.next = Node(data[i])
        curr = curr.next

middle_element = find_middle_element(head)
print(middle_element)
