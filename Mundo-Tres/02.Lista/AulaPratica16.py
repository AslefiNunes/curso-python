'''num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort()
print(num)
num.sort(reverse = True)
print(num)
num.insert(3,2)
print(num)

if 5 in num:    
    num.remove(5)
else:
    print('Não localizei o numero ')

print(num)'''

'''valores = []

valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores:
    print(f'{valor}...', end = '')

for indeci, valor in enumerate(valores):
    print(f'\nNa possição {indeci} encontrei  o valor {valor}')

print('Final da lista! ')

novaLista = []

for i in range(0, 5):
    novaLista.append(int(input(f'Digite o {i + 1}º valor: ')))

novaLista.sort()
print(novaLista)

for indeci, valor in enumerate(novaLista):
    print(f'\nNa possição {indeci} encontrei  o valor {valor}')

print(novaLista)'''


a = [2,3,4,5,7]
b = a #Cria uma ligação entre as lista
b[2] = 8 

print(f'Lista A {a}')
print(f'Lista B {b}')

# Para não criar vinculo faz o que segue. 

c = [1,2,3,4,5]
d = c[:] # Recebeu uma copia
d[3] = 0 

print(f'Lista C {c}')
print(f'Lista D {d}')