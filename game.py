import random


def print_field(game_field):
    if len(game_field) == 9:
        for i in range(0, 9, 3):
            print('|'.join(game_field[i: i + 3]))
    elif len(game_field) == 36:
        for i in range(0, 36, 6):
            print('|'.join(game_field[i: i + 6]))
    elif len(game_field) == 81:
        for i in range(0, 81, 9):
            print('|'.join(game_field[i: i + 9]))


def print_result(player_wins, comp_wins, draw):
    if player_wins:
        print("Player wins.")
    elif comp_wins:
        print("Computer wins.")
    elif draw:
        print("It's a draw.")


def print_fail(text):
    print(text)


def print_comp_move(comp_move):
    print(f"Computer choose cell {comp_move}")


def print_queue(player_moves):
    if player_moves:
        print('Player is "X", Computer is "O". Player moves first.')
    else:
        print('Player is "O", Computer is "X". Computer moves first.')


def choose_field_size():
    field_size = str(input('Choose desired field size (3x3, 6x6, 9x9 or toss for random):\n')).lower()
    if field_size == 'toss':
        field_size = random.choice((9, 36, 81))
        game_field = [f'_{x:>2}_' for x in range(1, field_size + 1)]
        moves_list = list(range(1, field_size + 1))
    elif field_size in ('3x3', '3х3'):  # for eng and rus
        game_field = [f'_{x:>2}_' for x in range(1, 10)]
        moves_list = list(range(1, 10))
    elif field_size in ('6x6', '6х6'):  # for eng and rus
        game_field = [f'_{x:>2}_' for x in range(1, 37)]
        moves_list = list(range(1, 37))
    elif field_size in ('9x9', '9х9'):  # for eng and rus
        game_field = [f'_{x:>2}_' for x in range(1, 82)]
        moves_list = list(range(1, 82))
    else:
        text = 'You can choose only 3x3, 6x6, 9x9 or toss for size. Try again. \n'
        print_fail(text)
        return choose_field_size()
    return game_field, moves_list


def choose_destiny():
    player = str(input('Choose your destiny (x, o or toss for random):\n')).lower()
    if player == 'toss':
        player = random.choice(('_ X_', '_ O_'))
        comp = '_ O_' if player == '_ X_' else '_ X_'
    elif player in ('x', 'х'):  # for eng and rus
        player = '_ X_'
        comp = '_ O_'
    elif player in ('o', 'о'):  # for eng and rus
        player = '_ O_'
        comp = '_ X_'
    else:
        text = "You can use only X, O or toss. Try again.\n"
        print_fail(text)
        return choose_destiny()
    return player, comp


def determine_turn(player):
    if player == '_ X_':
        player_moves = True
        print_queue(player_moves)
        return player_moves
    else:
        player_moves = False
        print_queue(player_moves)
        return player_moves


def player_turn(player_sign, game_field, moves_list):
    text = 'You can choose your move only from available moves'
    try:
        player_move = int(input("Choose number of cell for move from available moves\n"))
        if player_move in moves_list:
            game_field[player_move - 1] = player_sign
            moves_list.remove(player_move)
            print_field(game_field)
        else:
            print_fail(text)
            print_field(game_field)
            return player_turn(player_sign, game_field, moves_list)
    except (ValueError, IndexError):
        print_fail(text)
        print_field(game_field)
        return player_turn(player_sign, game_field, moves_list)


def comp_turn(comp_sign, game_field, moves_list):
    comp_move = random.choice(moves_list)
    print_comp_move(comp_move)
    game_field[comp_move - 1] = comp_sign
    moves_list.remove(comp_move)
    print_field(game_field)


def check_winner_3x3(player_sign, game_field, moves_list, game):
    player_wins = False
    comp_wins = False
    draw = False
    for i in range(0, 9, 3):
        if game_field[i] == game_field[i + 1] == game_field[i + 2]:
            game = False
            if game_field[i] == player_sign:
                player_wins = True
            else:
                comp_wins = True
    for i in range(0, 3):
        if game_field[i] == game_field[i + 3] == game_field[i + 6]:
            game = False
            if game_field[i] == player_sign:
                player_wins = True
            else:
                comp_wins = True
    if game_field[0] == game_field[4] == game_field[8]:
        game = False
        if game_field[0] == player_sign:
            player_wins = True
        else:
            comp_wins = True
    if game_field[2] == game_field[4] == game_field[6]:
        game = False
        if game_field[2] == player_sign:
            player_wins = True
        else:
            comp_wins = True
    if len(moves_list) == 0 and game is True:
        game = False
        draw = True
    print_result(player_wins, comp_wins, draw)
    return game


def check_winner_6x6(player_sign, game_field, moves_list, game):
    player_wins = False
    comp_wins = False
    draw = False
    for i in range(0, 36, 6):
        if game_field[i] == game_field[i + 1] == game_field[i + 2] == game_field[i + 3] == game_field[i + 4] == \
                game_field[i + 5]:
            game = False
            if game_field[i] == player_sign:
                player_wins = True
            else:
                comp_wins = True
    for i in range(0, 6):
        if game_field[i] == game_field[i + 6] == game_field[i + 12] == game_field[i + 18] == game_field[i + 24] == \
                game_field[i + 30]:
            game = False
            if game_field[i] == player_sign:
                player_wins = True
            else:
                comp_wins = True
    if game_field[0] == game_field[7] == game_field[14] == game_field[21] == game_field[28] == game_field[35]:
        game = False
        if game_field[0] == player_sign:
            player_wins = True
        else:
            comp_wins = True
    if game_field[5] == game_field[10] == game_field[15] == game_field[20] == game_field[25] == game_field[30]:
        game = False
        if game_field[5] == player_sign:
            player_wins = True
        else:
            comp_wins = True
    if len(moves_list) == 0 and game is True:
        game = False
        draw = True
    print_result(player_wins, comp_wins, draw)
    return game


def check_winner_9x9(player_sign, game_field, moves_list, game):
    player_wins = False
    comp_wins = False
    draw = False
    for i in range(0, 81, 9):
        if game_field[i] == game_field[i + 1] == game_field[i + 2] == game_field[i + 3] == game_field[i + 4] == \
                game_field[i + 5] == game_field[i + 6] == game_field[i + 7] == game_field[i + 8]:
            game = False
            if game_field[i] == player_sign:
                player_wins = True
            else:
                comp_wins = True
    for i in range(0, 9):
        if game_field[i] == game_field[i + 9] == game_field[i + 18] == game_field[i + 27] == game_field[i + 36] == \
                game_field[i + 45] == game_field[i + 54] == game_field[i + 63] == game_field[i + 72]:
            game = False
            if game_field[i] == player_sign:
                player_wins = True
            else:
                comp_wins = True
    if game_field[0] == game_field[10] == game_field[20] == game_field[30] == game_field[40] == game_field[50] == \
            game_field[60] == game_field[70] == game_field[80]:
        game = False
        if game_field[0] == player_sign:
            player_wins = True
        else:
            comp_wins = True
    if game_field[8] == game_field[16] == game_field[24] == game_field[32] == game_field[40] == game_field[48] == \
            game_field[56] == game_field[64] == game_field[72]:
        game = False
        if game_field[8] == player_sign:
            player_wins = True
        else:
            comp_wins = True
    if len(moves_list) == 0 and game is True:
        game = False
        draw = True
    print_result(player_wins, comp_wins, draw)
    return game


def check_winner_choosing(game_field, player_sign, moves_list, game):
    if len(game_field) == 9:
        game = check_winner_3x3(player_sign, game_field, moves_list, game)
    elif len(game_field) == 36:
        game = check_winner_6x6(player_sign, game_field, moves_list, game)
    elif len(game_field) == 81:
        game = check_winner_9x9(player_sign, game_field, moves_list, game)
    return game


def game_func(game_field, player_moves, player_sign, comp_sign, moves_list):
    game = True
    print_field(game_field)
    while game:
        if player_moves:
            player_turn(player_sign, game_field, moves_list)
            game = check_winner_choosing(game_field, player_sign, moves_list, game)
            if not game:
                break
            comp_turn(comp_sign, game_field, moves_list)
            game = check_winner_choosing(game_field, player_sign, moves_list, game)
        else:
            comp_turn(comp_sign, game_field, moves_list)
            game = check_winner_choosing(game_field, player_sign, moves_list, game)
            if not game:
                break
            player_turn(player_sign, game_field, moves_list)
            game = check_winner_choosing(game_field, player_sign, moves_list, game)


# TODO try to add logic to comp moves
# TODO refactor to DRY
def main():
    game_field, moves_list = choose_field_size()
    player_sign, comp_sign = choose_destiny()
    player_moves = determine_turn(player_sign)
    if len(moves_list) == 9:
        game_func(game_field, player_moves, player_sign, comp_sign, moves_list)
    elif len(moves_list) == 36:
        game_func(game_field, player_moves, player_sign, comp_sign, moves_list)
    elif len(moves_list) == 81:
        game_func(game_field, player_moves, player_sign, comp_sign, moves_list)


if __name__ == '__main__':
    main()
