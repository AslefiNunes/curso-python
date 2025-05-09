n = [0] * 4
for c in range (0, 4):
    escolha = int(input(f'Digite o index {c}º da TUPULA: '))
    n[c] = escolha

new_tup = tuple(n)

print(f'O Valor 9 apareceu {new_tup.count(9)} vezes')
print('Não possui valor 3' if 3 not in new_tup else f'O numero 3 apareceu na {new_tup.index(3) + 1}º')

for par in new_tup:
    if par % 2 == 0: 
        print(par, end = ' ')


n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o ultimo valor valor: '))

tup = (n1,n2,n3,n4)

print(f' O numero 9 aparecereceu {tup.count(9)} vezes')
print('Não possui valor 3' if 3 not in tup else f'O numero 3 esta na {tup.index(3) + 1}º posição')

for i in tup:
    if i % 2 == 0:
        print(i, end = ', ')