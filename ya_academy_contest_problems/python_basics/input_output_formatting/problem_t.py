N = int(input(""))
M = int(input(""))
K1 = int(input(""))
K2 = int(input(""))
m1 = N * (K2 - M) / (K2 - K1)
m2 = N - m1
print(int(m1), int(m2))
