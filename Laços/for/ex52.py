# leia numero e verifica se primo - divide apenas por 1 e por ele mesmo.
from time import sleep

n = int(input('Digite um número inteiro: '))
identificar = 0
for i in range(1, n+1):

    if n % i == 0:
        print('\033[34m', end='')
        identificar += 1
    else:
        print('\033[m', end='')

    print(f'{i} ', end=' ')

if identificar == 2 :
    print(f'\033[m O número {n} é primo.')