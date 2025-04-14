# refazer ex09 da tabuada. utilizando laços.

tabuada = int(input('Escolha um numero real inteiro para ver sua tabuada: '))

for i in range (1, 11):
    print('{} x {} = {}' .format(i, tabuada, (i*tabuada)))