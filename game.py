import random


def print_field(game_field):
    print('|'.join(game_field[0:3]))
    print('|'.join(game_field[3:6]))
    print('|'.join(game_field[6:9]))


def choose_destiny():
    p = str(input('Choose your destiny (x, o or toss for random):')).lower()
    if p == 'toss':
        p = random.choice(('X', 'O'))
        c = 'O' if p == 'X' else 'X'
    elif p in ('x', 'х'):  # for eng and rus
        p = 'X'
        c = 'O'
    elif p in ('o', 'о'):  # for eng and rus
        p = 'O'
        c = 'X'
    else:
        print("You can use only X, O or toss. Try again.")
        return choose_destiny()
    return p, c


#def move(p, c, game_field, moves_list):
#    if p == 'X':
#        player_move = str(input("Choose number of cell for move" + moves_list))




def main():
    game_field = ['_1_', '_2_', '_3_',
                  '_4_', '_5_', '_6_',
                  '_7_', '_8_', '_9_']
    moves_list = range(1, 10)
    print_field(game_field)
    player, comp = choose_destiny()
    #print(player, comp)

if __name__ == '__main__':
    main()
