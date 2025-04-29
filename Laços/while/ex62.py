n = int(input('Digite o primeiro termo: '))
p = int(input('Digite a razão: '))
decimo_termo = 0

while decimo_termo < 11:
    print(n, end =" ")
    n += p
    decimo_termo += 1
    if decimo_termo == 10:
        print()
        escolha = str(input(f'Gostaria de mudar o termo ? [S/N]: ')).upper().strip()
        if escolha == 'S':
            n = int(input('Digite o primeiro termo: '))
            p = int(input('Digite a razão: '))
            decimo_termo = 0
        else:
            print('0 Termos')
            break




""" Minha Solução

n = int(input('Digite o primeiro termo: '))
p = int(input('Digite a razão: '))
decimo_termo = n + (10-1) * p

while True:
    print(n, end =" ")
    n += p
    if n == decimo_termo:
        print(n, end =" ")
        print()
        escolha = str(input(f'Gostaria de mudar o termo ? [S/N]: ')).upper().strip()
        if escolha == 'S':
            n = int(input('Digite o primeiro termo: '))
            p = int(input('Digite a razão: '))
            decimo_termo = n + (10-1) * p
        else:
            print('0 Termos')
            break
"""
