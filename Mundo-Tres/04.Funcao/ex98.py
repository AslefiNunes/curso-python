from time import sleep
'''
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
        break'''
controleTempo = 0.1

def linha():
    print('-='*30)


linha()
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(controleTempo)
            cont += p
        print('FIM!')
        linha( )
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end =' ', flush=True)
            sleep(controleTempo)
            cont -= p
        print('FIM!')
        linha()


contador(1, 10, 1)
contador(10, 1 , 2)
print('Agora é suavez de personalizar a contagem!')
inicio = int(input('Início: '))
final = int(input('Fim: '))
pulo = int(input('Passo: '))
contador(inicio, final, pulo) 
