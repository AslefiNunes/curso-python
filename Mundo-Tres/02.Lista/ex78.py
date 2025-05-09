'''
RESPOSTA GUSTAVO EX 78 

num = []
indexMaior = []
indexMenor = []
print('Vamos ler 5 valores e guardalos em um lista.')

for i in range(0, 4):
    num.append(int(input(f'Digite o {i + 1}º valor: ')))
    if i == 3:
        maiorValor = max(num)
        menorValor = min(num)
        for ind, valor in enumerate(num):
            if valor == maiorValor:
                indexMaior.append(ind)
            if valor == menorValor:
                indexMenor.append(ind)

print(f' sua lista contem os seguintes numeros {num}')

print(f'O meu maior valor foi {maiorValor} nos INDEX {indexMaior}')
print(f'O meu menor valor foi {menorValor} nos INDEX {indexMenor}')
'''

'''
listNum = []
valor = 0

for i in range (0,5):
    valor = int(input('Digite um valor: '))
    if valor not in listNum:
        listNum.append(valor)

listNum.sort()
print(listNum)'''

num = list()
valor = 0

for i in range(0,5):
    valor = int(input('Digite um valor: '))
    if i == 0:
        num.append(valor)
    else:
        if valor > num[0]:
            num.append(valor)
        else:
            num.insert(0, valor)

print(num)