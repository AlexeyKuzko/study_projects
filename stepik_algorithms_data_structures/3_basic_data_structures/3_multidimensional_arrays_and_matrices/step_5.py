def create_minesweeper_field(N, M, W, mines):
    # Создаем поле, заполненное нулями
    field = [[0 for _ in range(M)] for _ in range(N)]

    # Устанавливаем мины на поле
    for mine in mines:
        x, y = mine
        field[x][y] = "*"  # Устанавливаем мину

        # Обновляем счетчик вокруг мин
        for i in range(max(0, x - 1), min(N, x + 2)):
            for j in range(max(0, y - 1), min(M, y + 2)):
                if field[i][j] != "*":
                    field[i][j] += 1

    return field


def print_field(field):
    for row in field:
        print(" ".join(str(cell) for cell in row))


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().strip().splitlines()

    # Чтение входных данных
    N, M = map(int, data[0].split())
    W = int(data[1])
    mines = [tuple(map(int, line.split())) for line in data[2 : 2 + W]]

    # Преобразуем координаты мин к нулевому индексу
    mines = [(x - 1, y - 1) for (x, y) in mines]

    # Создаем поле и выводим его
    field = create_minesweeper_field(N, M, W, mines)
    print_field(field)
