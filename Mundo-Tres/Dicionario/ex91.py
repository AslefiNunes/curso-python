from random import randint
from operator import itemgetter
from time import sleep

'''jogadores  = dict()

jog01 = randint(1,6)
jog02 = randint(1,6)
jog03 = randint(1,6)
jog04 = randint(1,6)


jogadores['play1'] = jog01
jogadores['play2'] = jog02
jogadores['play3'] = jog03
jogadores['play4'] = jog04

for k, v in jogadores.items():
    print(f'O {k} tirou o numero {v} do dado')'''

jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
rankin = list()

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')

rankin = sorted(jogo.items(), key = itemgetter(1), reverse=True)

for i, v in enumerate(rankin):
    print(f'{i +1} lugar: {v[0]} tirou {v[1]}')
    sleep(1)

