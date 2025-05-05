from time import sleep

def linha():
    print('-='*30)

linha()
def contador(inic, fim, passo):
    
    if inic > fim and passo > 0:
        passo = -passo
    if passo == 0:
        passo = 1
        if inic > fim:
            passo = -passo
    print(f'Contagem de {inic} até {fim} de {abs(passo)} em {abs(passo)}')
    for i in range(inic, fim, passo):
        print(f'{i}', end = ' ')
    print()
    linha()


contador(1, 10 , 1)
contador(10, 0, 2)
cont = 0
while True:

    cont +=1
    print('Agora é suavez de personalizar a contagem!')

    inicio = int(input('Início: '))
    final = int(input('Fim: '))
    pulo = int(input('Passo: '))
    linha()
    contador(inicio, final, pulo)

    if cont >= 4:
        break