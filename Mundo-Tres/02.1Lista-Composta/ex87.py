'''matriz = [[], [], []]
maiorValor = somaPar = somaColTre = cont = 0

for i in range(0,9):
    if i <= 2:
        matriz[0].append(int(input(f'Digite o valor em [{0,cont}]')))
    elif i >=3 and i <=5:
        matriz[1].append(int(input(f'Digite o valor em [{1,cont}]')))
    elif i > 5:
        matriz[2].append(int(input(f'Digite o valor em [{2,cont}]')))
    
    cont += 1
    if cont > 2:
        cont = 0
linha = int(input('Qual linha voce gostaria de saber o maior Valor ?: [0,1,2]: '))
seguLinha = matriz[linha]

for perco_Mat in matriz:
    print(perco_Mat)
    for perco_Lis in perco_Mat:
        if perco_Lis % 2 == 0:
            somaPar += perco_Lis
    somaColTre += perco_Mat[2]

for i in seguLinha:
    if i > maiorValor:
        maiorValor = i

print(f'O maior valor da seguanda Linha é {maiorValor}')
print(f'A soma dos valore par é {somaPar} e a soma da Terceira coluna é {somaColTre}')
'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
maior = spar = somacol = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor de [{l} {c}]: '))
        if matriz[l][c] % 2 == 0:
            spar +=matriz[l][c]

for i in matriz:
    print(i)
print(f'A soma dos valores pares são {spar}: ')
for l in range(0,3):
    somacol += matriz[l][2]
print(f'A soma dos valore da segunda coluna são {somacol}')
for l in range(0,3):
    if l == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')