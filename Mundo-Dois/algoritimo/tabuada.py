"""n = int(input('Digite um número para ver sua tabuada: '))

for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
    i += 1"""

num = int(input('Digite um núemro para ver seu fatorial: '))
C = num
F = 1

while True:
    F = F * C
    C -= 1
    if C == 0:
        print(f'O fatorial de {num} é {F}')
        para = str(input('Deseja parar? [S/N] ')).strip().upper()[0]
        if para == 'S':
            break
        else:
            C = int(input('Digite um núemro para ver seu fatorial: '))

