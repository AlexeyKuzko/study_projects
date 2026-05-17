"""Solution for Stepik course solutions: Generation Py / Professional / Chapter 4 / Part 4 1 / Step 12."""

import sys


def determine_winner():
    moves = list(map(int, sys.stdin.read().split()))
    last_move = moves[-1]
    total_moves = len(moves)

    # Определяем, кто сделал последний ход
    if total_moves % 2 == 1:
        last_player = "Анри"
        other_player = "Дима"
    else:
        last_player = "Дима"
        other_player = "Анри"

    # Проверяем чётность последнего хода
    if last_move % 2 == 0:
        print(last_player)
    else:
        print(other_player)


if __name__ == "__main__":
    determine_winner()
