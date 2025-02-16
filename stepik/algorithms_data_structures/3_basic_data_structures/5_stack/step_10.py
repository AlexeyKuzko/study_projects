from collections import deque


def play_war_game(player1_cards, player2_cards):
    player1 = deque(player1_cards)  # Очередь карт первого игрока
    player2 = deque(player2_cards)  # Очередь карт второго игрока
    max_moves = 10**6  # Максимально допустимое количество ходов
    moves = 0  # Счетчик ходов

    while player1 and player2 and moves < max_moves:
        moves += 1
        card1 = player1.popleft()  # Верхняя карта первого игрока
        card2 = player2.popleft()  # Верхняя карта второго игрока

        # Логика выигрыша: если 0 побеждает 9
        if card1 == 0 and card2 == 9:
            player1.extend([card1, card2])  # Победа первого игрока
        elif card2 == 0 and card1 == 9:
            player2.extend([card1, card2])  # Победа второго игрока
        elif card1 > card2:
            player1.extend([card1, card2])  # Победа первого игрока
        else:
            player2.extend([card1, card2])  # Победа второго игрока

    # Определение победителя или ничьи
    if len(player1) == 0:
        return "second", moves
    elif len(player2) == 0:
        return "first", moves
    else:
        return "botva", moves


# Чтение данных
player1_cards = list(map(int, input().split()))
player2_cards = list(map(int, input().split()))

# Запуск игры
winner, moves = play_war_game(player1_cards, player2_cards)
print(winner, moves)
