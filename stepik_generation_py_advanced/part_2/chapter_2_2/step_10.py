n = int(input().strip())

def is_infected(s):
    target = "anton"
    index = 0
    for char in s:
        if char == target[index]:
            index += 1
        if index == len(target):
            return True
    return False

infected_indices = []

for i in range(n):
    data = input().strip()
    if is_infected(data):
        infected_indices.append(i + 1)

if infected_indices:
    print(" ".join(map(str, infected_indices)))
