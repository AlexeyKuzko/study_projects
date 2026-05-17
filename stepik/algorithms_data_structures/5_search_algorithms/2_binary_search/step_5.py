"""Solution for Stepik course solutions: Algorithms Data Structures / 5 Search Algorithms / 2 Binary Search / Step 5."""


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


n = int(input())
books = []
for _ in range(n):
    books.append(input())

target_book = input()

if binary_search(books, target_book):
    print("YES")
else:
    print("NO")
