def chunked(lst, n):
    return [lst[i : i + n] for i in range(0, len(lst), n)]


s = input().split()
n = int(input())
print(chunked(s, n))
