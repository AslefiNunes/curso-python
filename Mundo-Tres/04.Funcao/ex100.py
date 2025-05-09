from random import randint

def sortear(lst):
    print(f'Sortenado 5 Valores da Lista', end = ' ')
    for i in range(0,5):
        lst.append(randint(1,10))
    for i in lst:
        print(f'{i}', end=' ')
    print('PRONTO !')
    

def somaPar(lst):
    soma = 0
    print('Os valores pares são:', end=' ')
    for i in lst:
        if i % 2 == 0:
            print(f'{i}', end=' ')
            soma += i
    print(f'e a soma é {soma}')


numeros = []
sortear(numeros)
somaPar(numeros)