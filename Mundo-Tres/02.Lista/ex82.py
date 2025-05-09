'''
RESPOSTA ASLEFI

body = []
par = []
impar = []
cont = 0
while True:
    valor = int(input('Digite um valor: '))
    cont += 1
    body.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

    if cont > 6:
        stop = str(input('Gostaria de PARA ? [S/N]: ')).strip().upper()[0]
        if stop == 'S':
            break


print(f'Esta é minha lista completa {body}')
print(f'Esta é a minha lista com os valores PAR {par}')
print(f'E esta é a lista dos Impares {impar}')
'''

num = list()
par = list()
impar = list()
cont = 0
while True:
    num.append(int(input('Digite o valor desejado: ')))
    cont += 1
    if cont > 6:
        stop = str(input('Gostaria de PARA ? [S/N]: ')).strip().upper()[0]
        if stop == 'S':
            break

for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print(num)
print(par)
print(impar)