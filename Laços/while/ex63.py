print('Sequencia de Fibonacci')
print('-' * 35)

controle  = int(input('Quantos termos voce que mostra ? '))
print('=' * 35)
n1 = 0
n2 = 1

print(n1,n2, end = ' ')
contador = 3
while contador <= controle:
    n3  = n1 + n2
    print(n3, end = ' ')
    n1 = n2
    n2 = n3
    contador += 1

print('Fim')
print('=' * 35)

''' Resposta Aslefi

controle = int(input('Quantidade de termo: '))
n1 = 0
n2 = 1
print(n1, n2, end = ' ')

while True:
    n3 = n1 + n2
    print(n3, end = ' ')
    n1 = n2
    n2 = n3
    if n1 >= controle:
        break'''

