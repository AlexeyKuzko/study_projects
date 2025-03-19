# Python
n = int(input())
used = set()
# Domain to use for emails
domain = "@beegeek.bzz"

# Read pre-issued email addresses
for _ in range(n):
    used.add(input().strip())

m = int(input())
new_employees = [input().strip() for _ in range(m)]

for name in new_employees:
    base_email = name + domain
    if base_email not in used:
        print(base_email)
        used.add(base_email)
    else:
        i = 1
        while name + str(i) + domain in used:
            i += 1
        new_email = name + str(i) + domain
        print(new_email)
        used.add(new_email)