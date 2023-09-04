start = int(input(""))
end = int(input(""))

if start <= end:
    step = 1
else:
    step = -1

for number in range(start, end + step, step):
    print(number, end=" ")
