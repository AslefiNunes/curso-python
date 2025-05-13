def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b    
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return 'Impossível dividir por zero'
    else:
        return a / b
def potenciacao(a, b):
    return a ** b

while True:
    print('Selecione a operação desejada:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Potenciação')
    print('6 - Sair')
    opcao = int(input('Digite sua opção (1/2/3/4/5/6): '))
    if opcao == 6:
        break
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    if opcao == 1:
        print(f' {a} + {b} = {soma(a, b)}')
    elif opcao == 2:
        print(f'{a} - {b} = {subtracao(a, b)}')
    elif opcao == 3:
        print(f' {a} x {b} = {multiplicacao(a, b)}')
    elif opcao == 4:
        print(f'{a} / {b} = {divisao(a, b)}')
    elif opcao == 5:
        print(f'{a} ** {b} = {potenciacao(a, b)}')
    else:
        print('Opção inválida')
