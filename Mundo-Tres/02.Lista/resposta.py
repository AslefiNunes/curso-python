'''
RESPOSTA DO GUSTAVO

listanum=[]
maior = 0
menor = 0

for c in range(0,5):
    listanum.append(int(input(f'Digite o item {c} da lista: ')))
    if c == 0:
        maior = listanum[c]
        menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if menor > listanum[c]:
            menor = listanum[c]

print(f'A milha lista é {listanum}')
print(f'O meu maior valor foi {maior} a posição', end = ' ')
for i,v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end = ' ')
print()
print(f'O meu menor valor foi {menor} na posição', end = ' ')
for i,v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end = ' ')'''


'''
RESPOSTA DO GUSTAVO

lista1 = []
valor  = 0

for i in range(0, 4):
    valor =  int(input('Digite um numero: '))
    if i == 0 or valor > lista1[-1]:
        lista1.append(valor)
        print(f'O {valor} foi para o final da lista')
    else:
        pos = 0
        while pos <= len(lista1):
            if valor < lista1[pos]:
                lista1.insert(pos, valor)
                print(f'O {valor} foi adicionado na posição {pos}')
                break
            pos += 1
print(lista1)'''

