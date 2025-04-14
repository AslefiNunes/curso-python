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

