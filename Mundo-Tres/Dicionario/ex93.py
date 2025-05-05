aprov = dict()

aprov['jogador'] = str(input('Digite o nome do jogar: '))
aprov['jogos'] = int(input(f'Digite quantos jogos o {aprov["jogador"]} jogou: '))
gols = list()

for i in range(0, aprov['jogos']):
    gols.append(int(input(f'{aprov["jogador"]} fez quantos gols no {i + 1}º jogo: ')))

aprov['gols'] = gols
aprov['total'] = sum(gols)

print('-='*30)
print(aprov)
print('-='*30)

for k, v in aprov.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
for i, v in enumerate(gols):
    print(f'=> Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {aprov['total']}')    



# RESPOSTA DO GUSTAVI

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Digite o nome do jogador.')).upper().strip()
tot = int(input('Digite o total de gols: '))

for i in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {i + 1}')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'=> Na partida {i} fez {v} gols.')
print(f'Foi um total de {jogador["total"]}')