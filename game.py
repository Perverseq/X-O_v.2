import random


def print_field(game_field):
    for i in range(3):
        print('|'.join(game_field[i:i+3]))


def choose_destiny():
    player = str(input('Choose your destiny (x, o or toss for random):')).lower()
    if player == 'toss':
        player = random.choice(('X', 'O'))
        comp = 'O' if player == 'X' else 'X'
    elif player in ('x', 'х'):  # for eng and rus
        player = 'X'
        comp = 'O'
    elif player in ('o', 'о'):  # for eng and rus
        player = 'O'
        comp = 'X'
    else:
        print("You can use only X, O or toss. Try again.")
        return choose_destiny()
    return player, comp


def move(p, c, game_field, moves_list):
    if p == 'X':
        try:
            player_move = int(input("Choose number of cell for move from available moves %s" % moves_list))
            game_field[player_move].replace('_X_')
            moves_list.pop(player_move)
        except ValueError:
            print('You can choose your move only from available moves')




def main():
    game_field = ['_1_', '_2_', '_3_',
                  '_4_', '_5_', '_6_',
                  '_7_', '_8_', '_9_']
    moves_list = list(range(1, 10))
    print_field(game_field)
    player_sign, comp_sign = choose_destiny()
    #print(player, comp)
    move(player_sign, comp_sign, game_field, moves_list)

if __name__ == '__main__':
    main()