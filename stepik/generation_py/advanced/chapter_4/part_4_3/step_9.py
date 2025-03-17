n = int(input())

nested_list = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]

for lst in nested_list:
    print(lst)
