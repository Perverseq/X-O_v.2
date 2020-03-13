import random


def print_field(game_field):
    print('|'.join(game_field[0:3]))
    print('|'.join(game_field[3:6]))
    print('|'.join(game_field[6:9]))


def choose_destiny():
    p = str(input('choose your destiny (x/o or toss for random):'))
    if p == 'toss':
        p = random.choice(('X', 'O'))
        c = 'O' if p == 'X' else 'X'
    elif p.lower() == 'x' or p.lower() == 'х':
        p = 'X'
        c = 'O'
    elif p.lower() == 'o' or p.lower() == 'о':
        p = 'O'
        c = 'X'
    else:
        print("Можно вводить только О, Х или toss. Попробуйте еще раз.")
        return choose_destiny()
    return p, c


def move(player, comp):
    pass


def main():
    game_field = ['_1_', '_2_', '_3_',
                  '_4_', '_5_', '_6_',
                  '_7_', '_8_', '_9_']
    moves_list = range(1, 10)
    print_field(game_field)
    player, comp = choose_destiny()


if __name__ == '__main__':
    main()
