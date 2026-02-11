"""
Напишите функцию декоратор, которая переводит значение декорируемой функции
в рублях
либо в доллары (курс: 1$ = 99 рублей)
либо в евро (курс: 1€ = 102 рубля)
либо в юани (курс: 1¥ = 14 рублей)
Для тех, кто хочет добавить знак валюты:
chr(36) -> '$'
chr(8364) -> '€'
chr(8381) -> '₽'
chr(165) -> '¥'

before decorating: 10000₽
after: 100€
"""

def currency(to: str):
    rates = {"USD": (99, chr(36)),
             "EUR": (102, chr(8364)),
             "CNY": (14, chr(165)),
             "RUB": (1, chr(8381))}
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            rate, symbol = rates[to]
            converted = round(float(result[:-1]) / rate, 2)  # из result убираем символ рубля, делим и округляем
            return f"{converted}{symbol}"
        return wrapper
    return decorator


@currency("USD")
def summa(count: float, price: float) -> str:
    """ Out: <float><CHAR>"""
    return f'{round(count * price, 2)}₽'

print(summa(49.5, 2))
print(summa(305.5, 2.4))
print(summa(1000, price=10))

