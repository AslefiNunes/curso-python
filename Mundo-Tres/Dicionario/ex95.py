'''
 RESPOSTA DO GUSTAVO

time = list()
aprov = dict()
gols = list()
soma  = 0

while True:
    aprov['jogador'] = str(input('Digite o nome do jogador: ')).upper().strip()
    part = int(input(f'Total de partidas de {aprov['jogador']}. '))
    for i in range(0, part):
        gols.append(int(input(f'Quantidade de gols na {i+1}º partida.')))
        soma += gols[i]
    aprov['gols'] = gols[:]
    aprov['total'] = soma
    time.append(aprov.copy())
    soma = 0
    gols.clear()
    cont = str(input('Deseja cadastra outro jogador ? [S/N]')).upper().strip()[0]
    if cont in 'N':
        break

print('-=' * 20)
print(f'{"cod"} ', end = '')
for i in aprov.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 20)
for i, v in enumerate(time):
    print(f'{i:>3} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
while True:
    escol = int(input('Escolha o cod do jogador: '))
    if escol == 999:
        break
    if escol >= len(time):
        print(f'Erro não existe jogador com codigo {escol}! Tente novamento ou digite 999 para sair' )
    else:
        print(f'-- Levantamento do jogador {time[escol]["nome"]}')
        for i, v in enumerate(time[escol]['gols']):
            print(f'  No jogo {i} fez {v} gols')
    print('-'*40)
    
print(f'Fim do Pograma!')'''