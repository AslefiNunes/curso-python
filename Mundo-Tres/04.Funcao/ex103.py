'''def ficha(nome = 'desconhecido', gols = 0):
    if len(nome) == 0:
        nome = 'desconhecido'
    print(f'O jogador {nome} fez {gols} no campeonato.')

nomeJogador = str(input('Nome do jogador: ')).strip()
numGols = str(input('numeros de gols: ')).strip()
if numGols.isnumeric():
    numGols = int(numGols)
else:
    numGols = 0
ficha(nomeJogador, numGols)'''


def ficha(nome = '<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: ')).strip()
g = str(input('Numero de Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
