def to_base_p(n, p):
    if n == 0:
        return ""
    else:
        return to_base_p(n // p, p) + str(n % p)


def main():
    P = int(input().strip())
    decimal_number = int(input().strip())

    # Получаем строку для P-ичной системы счисления
    base_p_number = to_base_p(decimal_number, P)

    # Обработка случая, когда число равно 0
    if decimal_number == 0:
        base_p_number = "0"

    # Формируем вывод в нужном формате
    output = f"{decimal_number}(10)={base_p_number}({P})"
    print(output)


if __name__ == "__main__":
    main()
