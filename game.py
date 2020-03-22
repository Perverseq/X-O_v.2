import random


def print_field(game_field):
    for i in range(0, 10, 3):
        print('|'.join(game_field[i: i + 3]))


def choose_destiny():
    player = str(input('Choose your destiny (x, o or toss for random):')).lower()
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
        print("You can use only X, O or toss. Try again.")
        return choose_destiny()
    return player, comp


def determine_turn(player):
    if player == '_X_':
        player_moves = True
        print('Player is "X", Computer is "O". Player moves first.')
        return player_moves
    else:
        player_moves = False
        print('Player is "O", Computer is "X". Computer moves first.')
        return player_moves


def player_turn(player_sign, game_field, moves_list):
    try:
        player_move = int(input(f"Choose number of cell for move from available moves {moves_list}"))
        if player_move in moves_list:
            game_field[player_move - 1] = player_sign
            moves_list.remove(player_move)
            print_field(game_field)
        else:
            print('You can choose your move only from available moves')
            return player_turn(player_sign, game_field, moves_list)
    except ValueError or IndexError:
        print('You can choose your move only from available moves')
        return player_turn(player_sign, game_field, moves_list)


def comp_turn(comp_sign, game_field, moves_list):
    comp_move = random.choice(moves_list)
    print(f"Computer choose cell {comp_move}")
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


def print_result(player_wins, comp_wins, draw):
    if player_wins:
        print("Player wins.")
    elif comp_wins:
        print("Computer wins.")
    elif draw:
        print("It's a draw.")


# TODO try to add logic to comp moves
# TODO refactor to DRY
# TODO choose game field 3x3 6x6 9x9
def main():
    game_field = ['_1_', '_2_', '_3_',
                  '_4_', '_5_', '_6_',
                  '_7_', '_8_', '_9_']
    moves_list = list(range(1, 10))

    player_sign, comp_sign = choose_destiny()
    player_moves = determine_turn(player_sign)
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


if __name__ == '__main__':
    main()
