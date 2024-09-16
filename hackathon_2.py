def get_player_names():
    player1_name = input("Введіть ім'я першого гравця: \n ")
    player2_name = input("Введіть ім'я другого гравця: \n ")
    return player1_name, player2_name


def display_field(game_field):
    for x in range(3):
        print("----------")
        for y in range(3):
            print("|", game_field[x * 3 + y], end=" ")
        print("|")
    print("----------")


def chose_pieces():
    pieces_number = input("Виберіть ким хочете грати X або O\n")
    while not pieces_number in ['X', 'O']:
        pieces_number = input("Введіть коректне значення\n")
    return pieces_number


def whos_winner(game_field):
    for i in range(3):
        if game_field[i * 3] == game_field[i * 3 + 1] == game_field[i * 3 + 2] and game_field[i * 3] in ('X', 'O'):
            return game_field[i * 3]
    for i in range(3):
        if game_field[i] == game_field[i + 3] == game_field[i + 6] and game_field[i] in ('X', 'O'):
            return game_field[i]
    if game_field[0] == game_field[4] == game_field[8] and game_field[0] in ('X', 'O'):
        return game_field[0]
    if game_field[2] == game_field[4] == game_field[6] and game_field[2] in ('X', 'O'):
        return game_field[2]
    if all(x in ('X', 'O') for x in game_field):
        return 'Нічия!'
    return False


def get_move(game_field):
    move = int(input("Виберіть номер клітинки (від 1 до 9) \n "))
    while not legal_move(game_field, move):
        move = int(input("Цей хід некоректний \n "))
    return move


def legal_move(game_field, player_move):
    legal = True
    if game_field[player_move - 1] in ['X', 'O']:
        legal = False
    return legal


def modify_field(game_field, user_piece, move):
    game_field[move - 1] = user_piece


def switch_turns(user_piece):
    if user_piece == 'X':
        user_piece = 'O'
    else:
        user_piece = 'X'
    return user_piece


def win_or_tie(user_piece, player1_name, player2_name):
    if user_piece == "Нічия!":
        print("Нічия!")
    else:
        if user_piece == 'X':
            winner_name = player1_name
        else:
            winner_name = player2_name
        print(f"Гравець {winner_name} виграв!")


def main():
    game_field = ["", "", "", "", "", "", "", "", ""]
    display_field(game_field)
    player1_name, player2_name = get_player_names()

    player_turn = chose_pieces()

    print(f"{player1_name} грає як 'X', {player2_name} грає як 'O' \n ")

    while not whos_winner(game_field):
        player_move = get_move(game_field)
        modify_field(game_field, player_turn, player_move)
        display_field(game_field)
        if not whos_winner(game_field):
            player_turn = switch_turns(player_turn)

    win_or_tie(player_turn, player1_name, player2_name)


if __name__ == "__main__":
    main()
