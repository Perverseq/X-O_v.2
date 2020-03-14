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


def player_x_turn(game_field, moves_list):
    print("X's turn.")
    #try:
    player_move = int(input("Choose number of cell for move from available moves %s" % moves_list))
    if player_move in moves_list:
        game_field[player_move - 1] = '_X_'  # TODO disable rewriting
        moves_list.remove(player_move)
        # print(moves_list)
        print_field(game_field)
    else:
        print('You can choose your move only from available moves')
        return player_x_turn(game_field, moves_list)
    #except IndexError:
    #    print('You can choose your move only from available moves')
    #    return player_x_turn(game_field, moves_list)
    #except ValueError:
    #    print('You can choose your move only from available moves')
    #    return player_x_turn(game_field, moves_list)


def player_o_turn(game_field, moves_list):
    print("O's turn.")
    #try:
    player_move = int(input("Choose number of cell for move from available moves %s" % moves_list))
    if player_move in moves_list:
        game_field[player_move - 1] = '_O_'  # TODO disable rewriting
        moves_list.remove(player_move)
        # print(moves_list)
        print_field(game_field)
    else:
        print('You can choose your move only from available moves')
        return player_o_turn(game_field, moves_list)
    #except IndexError:
    #    print('You can choose your move only from available moves')
    #    return player_o_turn(game_field, moves_list)
    #except ValueError:
    #    print('You can choose your move only from available moves')
    #    return player_o_turn(game_field, moves_list)


def comp_x_turn(game_field, moves_list):
    print("X's turn.")
    comp_move = random.choice(moves_list)
    print("Computer choose cell %d" % comp_move)
    game_field[comp_move - 1] = '_X_'
    moves_list.remove(comp_move)
    print_field(game_field)


def comp_o_turn(game_field, moves_list):
    print("O's turn.")
    comp_move = random.choice(moves_list)
    print("Computer choose cell %d" % comp_move)
    game_field[comp_move - 1] = '_O_'
    moves_list.remove(comp_move)
    print_field(game_field)


def check_winner(player_sign, game_field, moves_list, game):
    try:
        for i in range(0, 9, 3):
            if game_field[i] == game_field[i + 1] == game_field[i + 2]:
                game = False
                if game_field[i] == player_sign:
                    print("Player wins.")
                else:
                    print("Computer wins.")
        for i in range(0, 3):
            if game_field[i] == game_field[i + 3] == game_field[i + 6]:
                game = False
                if game_field[i] == player_sign:
                    print("Player wins.")
                else:
                    print("Computer wins.")
        if game_field[0] == game_field[4] == game_field[8]:
            game = False
            if game_field[0] == player_sign:
                print("Player wins.")
            else:
                print("Computer wins.")
        if game_field[2] == game_field[4] == game_field[6]:
            game = False
            if game_field[2] == player_sign:
                print("Player wins.")
            else:
                print("Computer wins.")
    except ValueError:
        if not moves_list:
            game = False
            print("It's a draw.")
    return game


# TODO try to add logic to comp moves
# TODO refactor to DRY
def main():
    game_field = ['_1_', '_2_', '_3_',
                  '_4_', '_5_', '_6_',
                  '_7_', '_8_', '_9_']
    moves_list = list(range(1, 10))

    player_sign, comp_sign = choose_destiny()
    #print(player, comp)
    player_moves = determine_turn(player_sign)
    game = True
    print_field(game_field)
    while game:
        if player_moves:
            player_x_turn(game_field, moves_list)
            game = check_winner(player_sign, game_field, moves_list, game)
            if not game:
                break
            comp_o_turn(game_field, moves_list)
            game = check_winner(player_sign, game_field, moves_list, game)
        else:
            comp_x_turn(game_field, moves_list)
            game = check_winner(player_sign, game_field, moves_list, game)
            if not game:
                break
            player_o_turn(game_field, moves_list)
            game = check_winner(player_sign, game_field, moves_list, game)



if __name__ == '__main__':
    main()
