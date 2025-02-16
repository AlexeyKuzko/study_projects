n = int(input())
m = int(input())

mult = [[i * j for j in range(m)] for i in range(n)]

for row in mult:
    print(" ".join(str(x).ljust(3) for x in row))
