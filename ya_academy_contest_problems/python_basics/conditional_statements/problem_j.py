password = input()
sum_least_significant = int(password[1]) + int(password[2])
sum_most_significant = int(password[0]) + int(password[1])
new_number = str(max(sum_least_significant, sum_most_significant)) + str(
    min(sum_least_significant, sum_most_significant)
)

print(new_number)
