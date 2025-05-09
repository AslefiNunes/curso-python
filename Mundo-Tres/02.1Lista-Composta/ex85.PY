'''num = []
par = []
impar = []
valor = 0

for i in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

par.sort()
impar.sort()
num.append(par[:])
num.append(impar[:])
par.clear
impar.clear
print(num)'''

#RESPOSTA DO GUSTAVO. 
num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print(f'Os valore pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')