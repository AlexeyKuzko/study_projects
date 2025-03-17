sequence = input().strip()
max_count = 0
current_count = 0

for char in sequence:
    if char == 'Р':
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print(max_count)