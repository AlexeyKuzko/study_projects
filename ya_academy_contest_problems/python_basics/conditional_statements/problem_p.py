p = int(input())
v = int(input())
t = int(input())
first = max(p, v, t)
second = 0
third = min(p, v, t)
if p != first and p != third:
    second = "Петя"
elif v != first and v != third:
    second = "Вася"
elif t != first and t != third:
    second = "Толя"
if p == first:
    first = "Петя"
elif v == first:
    first = "Вася"
elif t == first:
    first = "Толя"
if p == third:
    third = "Петя"
elif v == third:
    third = "Вася"
elif t == third:
    third = "Толя"
print(
    f"{' ' * 10}{first}{' ' * 10}\n{' ' * 2}{second}{' ' * 18}\n{' ' * 18}{third}{' ' * 2}"
)
print(f"{' ' * 3}II{' ' * 6}I{' ' * 6}III{' ' * 2}")
