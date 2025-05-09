
print('-='* 30)
def maior(lst):
    print('Analisando valores passados...')
    for i in lst:
        print(f'{i}, ', end='')
    print(f'foram informados {len(lst)} valores ao todo.')
    print(f'O maior valor informado é {max(lst)}')
    print('-='* 30)
    

lista1 = [2, 9, 4, 5, 7, 1]
lista2 = [4, 7, 0]
lista3 = [1, 2]

maior(lista1)
maior(lista2)
maior(lista3)
'''
print('-='* 30)
def maior(lst):
    print('Analisando valores passados...')
    for i in lst:
        print(f'{i}, ', end='')
    print(f'foram informados {len(lst)} valores ao todo.')
    print(f'O maior valor informado é {max(lst)}')
    print('-='* 30)
    

lista1 = [2, 9, 4, 5, 7, 1]
lista2 = [4, 7, 0]
lista3 = [1, 2]

maior(lista1)
maior(lista2)
maior(lista3)'''

print('-='* 30)
def maior(*lst):
    maiorValor = 0
    print('Analisando valores passados...')
    for i in lst:
        print(f'{i}, ', end='')
        if i >= maiorValor:
            maiorValor = i
    print(f'foram informados {len(lst)} valores ao todo.')
    print(f'O maior valor informado é {maiorValor}')
    print('-='* 30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
