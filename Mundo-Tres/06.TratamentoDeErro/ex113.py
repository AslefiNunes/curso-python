def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! digite um número inteiro válido.')
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario.')
            return 0
        else:
            while True:
                try:
                    real = float(input('Digite um numero Real: '))
                except Exception as erro:
                    print(f'Erro! {erro.__class__}')
                else:
                    print(f'O valor interio digitado foi {num} e o real foi {real}')
                    return 0
            

n = leiaInt('Digite um numero Inteiro: ')
