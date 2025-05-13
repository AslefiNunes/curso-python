from random import randint
# Exercicio 68 - Jogo de PAR ou IMPAR
# Faça um programa que jogue PAR ou ÍMPAR com o computador. O jogo só termina quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    while jogador < 0 or jogador > 10:
        print('Número inválido! Escolha um número entre 0 e 10.')
        jogador = int(input('Digite um valor: '))
    cpu = randint(0, 10)
    total = jogador + cpu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {cpu}. total de {total}', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break

print(f'Você venceu {cont} vezes consecutivas.')

''' Minha resposta
from random import randint

print('=' * 50)
print('Vamos Jogar PAR ou IMPAR as regras são: \n 1º Escolher valores entre 0 e 10 e PAR ou IMPAR \n 2º O jogo só apra se você vencer a maquina \n 3º Qualquer valor não valido sera tido como desistencia.\n 4º O mais importante é se divertir')
print('=' * 50)

while True:
    escolha_jogador = str(input('Escolha entre PAR e IMPAR: ')).upper().strip()

    if escolha_jogador not in ('PAR', 'IMPAR'):
        print(f'O Valor {escolha_jogador} não é valido fere a 1º Regra, VOCÊ PERDEU !!')
        break

    numero_jogador = int(input('Qual o numero (0 a 10): '))
    if not 0 <= numero_jogador <= 10:
        print('Número inválido! Escolha um número entre 0 e 10.')
        continue # Volta para o início do loop para nova tentativa

    numero_cpu = randint(0, 10)
    soma = numero_jogador + numero_cpu
    resultado = 'PAR' if soma % 2 == 0 else 'IMPAR'
    escolha_cpu = 'IMPAR' if escolha_jogador == 'PAR' else 'PAR'

    print(f'Você jogou {numero_jogador} e escolheu {escolha_jogador}. O computador jogou {numero_cpu} e escolheu {escolha_cpu}. Total = {soma}, que é {resultado}.')

    if resultado == escolha_jogador:
        print('Você VENCEU!')
        break
    else:
        print('Você PERDEU! Tente novamente.')'''