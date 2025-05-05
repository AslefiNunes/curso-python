from time import sleep

def linha():
    print('-=' * 30)

def contador(inic, fim, passo):
    print(f'Contagem de {inic} até {fim} de {abs(passo)} em {abs(passo)}')
    if passo == 0:
        passo = 1 if inic < fim else -1

    if inic < fim and passo < 0:
        passo = abs(passo)
    elif inic > fim and passo > 0:
        passo = -abs(passo)

    for i in range(inic, fim + (1 if inic < fim else -1), passo):
        print(f'{i}', end=' ')
    print()
    linha()

linha()
contador(1, 10, 1)
contador(10, 0, -2)
contador(20, 0, 2)
linha()

cont = 0
while cont < 4:
    cont += 1
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    final = int(input('Fim: '))
    pulo = int(input('Passo: '))
    linha()
    contador(inicio, final, pulo)

print("Fim do programa.")