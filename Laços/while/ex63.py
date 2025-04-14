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
        break

