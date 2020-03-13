import random


def choose_destiny():
    #comp = ''
    player = str(input('choose your destiny (x/o or toss for random):'))
    if player == 'toss':
        player = random.choice(('X', 'O'))
        #print(player, end='\n')
        comp = 'O' if player == 'X' else 'X'
        #print(comp, end='\n')
    elif player.lower() == 'x' or player.lower() == 'х':
        player = 'X'
        comp = 'O'
    elif player.lower() == 'o' or player.lower() == 'о':
        player = 'O'
        comp = 'X'
    else:
        print("Можно вводить только О, Х или toss. Попробуйте еще раз.")
        player = ''
        comp = ''
        choose_destiny()
    return player, comp

#TODO Разобраться с else.
#player1, comp1 = choose_destiny()
#print(player1, comp1)

#a = random.choice(('X', 'O'))
#print(a)
