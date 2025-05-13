condicao = False
S = 0

while condicao == False:
    N = int(input('Digite um número: '))
    S = S + N
    para = str(input('Deseja parar? [S/N] ')).strip().upper()[0]
    if para == 'S':
        condicao = True

print(f'A soma dos números digitados é {S}')


