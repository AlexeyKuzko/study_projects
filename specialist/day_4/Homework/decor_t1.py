"""
Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
Пример 1:
********
*Привет*
********
Пример 2:
****
*23*
****
Пример 3:
**************
*[34, 45, 12]*
**************
"""

def stars_frame(func_to_decor):
    def wrapper(*args, **kwargs):
        result = func_to_decor(*args, **kwargs)
        text = str(result)
        border = "*" * (len(text) + 2)
        return f"{border}\n*{text}*\n{border}"
    return wrapper


@stars_frame
def func(arg):
    return arg

@stars_frame
def func_two(arg1, arg2):
    return f'Output: {arg1.capitalize()} {arg2.upper()}'


# Тестовая часть
print(f"{func('Привет')}\n") # обернул в f-строки, чтобы добавить пустые строки между выводами и они не "слипались"
print(f"{func(23)}\n")
print(f"{func([34, 45, 12])}\n")
print(f"{func(arg=100)}\n")
print(f"{func_two('hello ', 'python')}\n")
# эксперимент
print(f"{func_two(func('пРИВЕТ'), 'python')}\n") # декорирован каждый вызов функций => 'привет' не capitalize
