import random


def print_field(game_field):
    if len(game_field) == 9:
        for i in range(0, 10, 3):
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


def print_destiny_fail():
    print("You can use only X, O or toss. Try again.\n")


def print_move_fail():
    print('You can choose your move only from available moves')


def print_comp_move(comp_move):
    print(f"Computer choose cell {comp_move}")


def print_queue(player_moves):
    if player_moves:
        print('Player is "X", Computer is "O". Player moves first.')
    else:
        print('Player is "O", Computer is "X". Computer moves first.')


def print_size_fail():
    print('You can choose only 3x3, 6x6, 9x9 or toss for size. Try again. \n')


def choose_field_size():
    field_size = str(input('Choose desired field size (3x3, 6x6, 9x9 or toss for random):\n')).lower()
    if field_size == 'toss':
        field_size = random.choice((9, 36, 81))
        game_field = [f'_{x}_' for x in range(1, field_size + 1)]
    elif field_size in ('3x3', '3х3'): # for eng and rus
        game_field = [f'_{x}_' for x in range(1, 10)]
    elif field_size in ('6x6', '6х6'): # for eng and rus
        game_field = [f'_{x}_' for x in range(1, 37)]
    elif field_size in ('9x9', '9х9'): # for eng and rus
        game_field = [f'_{x}_' for x in range(1, 82)]
    else:
        print_size_fail()
        return choose_field_size()
    return game_field


def choose_destiny():
    player = str(input('Choose your destiny (x, o or toss for random):\n')).lower()
    if player == 'toss':
        player = random.choice(('_X_', '_O_'))
        comp = '_O_' if player == '_X_' else '_X_'
    elif player in ('x', 'х'):  # for eng and rus
        player = '_X_'
        comp = '_O_'
    elif player in ('o', 'о'):  # for eng and rus
        player = '_O_'
        comp = '_X_'
    else:
        print_destiny_fail()
        return choose_destiny()
    return player, comp


def determine_turn(player):
    if player == '_X_':
        player_moves = True
        print_queue(player_moves)
        return player_moves
    else:
        player_moves = False
        print_queue(player_moves)
        return player_moves


def player_turn(player_sign, game_field, moves_list):
    try:
        player_move = int(input(f"Choose number of cell for move from available moves {moves_list}\n"))
        if player_move in moves_list:
            game_field[player_move - 1] = player_sign
            moves_list.remove(player_move)
            print_field(game_field)
        else:
            print_move_fail()
            return player_turn(player_sign, game_field, moves_list)
    except (ValueError, IndexError):
        print_move_fail()
        print_field(game_field)
        return player_turn(player_sign, game_field, moves_list)


def comp_turn(comp_sign, game_field, moves_list):
    comp_move = random.choice(moves_list)
    print_comp_move(comp_move)
    game_field[comp_move - 1] = comp_sign
    moves_list.remove(comp_move)
    print_field(game_field)


def check_winner(player_sign, game_field, moves_list, game):
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


def game_3x3(game_field, player_moves, player_sign, comp_sign, moves_list):
    game = True
    print_field(game_field)
    while game:
        if player_moves:
            player_turn(player_sign, game_field, moves_list)
            game = check_winner(player_sign, game_field, moves_list, game)
            if not game:
                break
            comp_turn(comp_sign, game_field, moves_list)
            game = check_winner(player_sign, game_field, moves_list, game)
        else:
            comp_turn(comp_sign, game_field, moves_list)
            game = check_winner(player_sign, game_field, moves_list, game)
            if not game:
                break
            player_turn(player_sign, game_field, moves_list)
            game = check_winner(player_sign, game_field, moves_list, game)


# TODO try to add logic to comp moves
# TODO refactor to DRY
# TODO choose game field 3x3 6x6 9x9
def main():
    game_field = choose_field_size()
    moves_list = list(range(1, 10))
    player_sign, comp_sign = choose_destiny()
    player_moves = determine_turn(player_sign)
    game_3x3(game_field, player_moves, player_sign, comp_sign, moves_list)


if __name__ == '__main__':
    main()
