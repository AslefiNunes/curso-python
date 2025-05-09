from random import randint


def jogos_Mega():
    print('-'*30)
    print('JOGAR NA MEGA SENA')
    print('-'*30)

    quantJogos = int(input('Digite quantos jogos você quer: '))

    print(f'-=-=-= SORTENADO {quantJogos} JOGOS-=-=-=')

    jogos = []
    dados = []
    num = 0
    for i in range(0, quantJogos):
        while True:
            num = randint(1, 60)
            if num not in dados:
                dados.append(num)
            if len(dados) == 6:
                dados.sort()
                jogos.append(dados[:])
                dados.clear()
                break
        

    for i in jogos:
        print(f'Jogo: {i}')

    print(f'{'-='*5} BOA SORTE! {'-='*5}')

while True:
    play = str(input('Vamos sortear os valores para jogar ?: ')).upper().strip()[0]
    if 'S' in play:
        jogos_Mega()
    elif 'N' in play:
        print('Fim do Programa! ')
        break

