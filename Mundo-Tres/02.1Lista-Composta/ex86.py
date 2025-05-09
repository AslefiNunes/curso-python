'''matriz = [[],[],[]]
cont = 0
for i in range(0,9):
    if i <= 2:
        matriz[0].append(int(input(f'Digite o valor em [{0, cont}]: ')))
    elif i >=3 and i <= 5:
        matriz[1].append(int(input(f'Digite o valor em [{1, cont}]: ')))
    else:
        matriz[2].append(int(input(f'Digite o valor em [{2, cont}]: ')))

    cont += 1
    if cont > 2:
        cont = 0

for i in matriz:
    print(i)'''


matriz = [[0,0,0], [0,0,0], [0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor  para [{l},{c}]: '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = ' ')
    print()