n = int(input())

first_quarter = 0
second_quarter = 0
third_quarter = 0
fourth_quarter = 0

for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        first_quarter += 1
    elif x < 0 and y > 0:
        second_quarter += 1
    elif x < 0 and y < 0:
        third_quarter += 1
    elif x > 0 and y < 0:
        fourth_quarter += 1

print(f"Первая четверть: {first_quarter}")
print(f"Вторая четверть: {second_quarter}")
print(f"Третья четверть: {third_quarter}")
print(f"Четвертая четверть: {fourth_quarter}")
