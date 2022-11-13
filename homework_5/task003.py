# Создайте программу для игры в "Крестики-нолики".

board = list(range(1, 10))
wins_coords = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print()
    print("\t     |     |")
    print(f"\t  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("\t_____|_____|_____")
    print("\t     |     |")
    print(f"\t  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("\t_____|_____|_____")
    print("\t     |     |")
    print(f"\t  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("\t     |     |")
    print()


def enter_value(player_token):
    while True:
        value = input(f"Куда поставить {player_token} ?: ")
        if value not in "123456789":
            print("Введена не корректная цифра. Попробуйте снова.")
            continue
        value = int(value)
        if str(board[value - 1]) in "XO":
            print("Эта клетка уже занята. Выберите другую.")
            continue
        board[value - 1] = player_token
        break


def check_win():
    for each in wins_coords:
        if board[each[0] - 1] == board[each[1] - 1] == board[each[2] - 1] != "":
            return board[each[1] - 1]
    else:
        return False


count = 0
while True:
    draw_board()
    if count % 2 == 0:
        enter_value("X")
    else:
        enter_value("O")
    if count > 3:
        winner = check_win()
        if winner:
            draw_board()
            print(f"Победил {winner}")
            break
    count += 1
    if count > 8:
        draw_board()
        print("Ничья!")
        break
