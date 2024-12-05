n = int(input())

list_of_lists = [[i for i in range(1, n + 1)] for _ in range(n)]

for lst in list_of_lists:
    print(lst)
