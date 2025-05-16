'''nome = 'Luis Otario'

cont = 0
while cont < len(nome):
    print(f'*{nome[cont]}', end = '')
    cont += 1
print('*')'''

# Crie uma calculadora com While - pergunto ao usuario 2 valores primeir é denominador peça tbm a operação que vai ser +, -, *, /

def escolha_operacao():
    print('Escolha uma das opeções:\n' \
            '[1] - Adição\n' \
            '[2] - Subitração\n' \
            '[3] - Multiplicação\n' \
            '[4] - Divisão\n ' \
            '')
    return int(input('Faça sua Escolha: '))

def tabuada(numero, operador):
    contador = 1
    print(f'\nTabuada {definindo_operacao(operador)} do numero {numero}\n')
    for i in range (1, 11):
        if operador == 1:
            print(f'{i} + {numero} = {i+numero}')
        elif operador == 2:
            print(f'{i+numero} - {numero} = {i}')
        elif operador == 3:
            print(f'{i} x {numero} = {i*numero}')
        else:
            print(f'{numero * i} / {numero} = {i}')
    print('')

def definindo_operacao(operacao):
    ope = {1: 'Adição', 2: 'subitração', 3: 'Mutiplicação', 4:'Divisão'}
    return ope.get(operacao, 'Operação Invalida')

def validar_entradas():
    while True:
        try:
            numero = int(input('Digite um valor para ver sua tabuada: '))
            operacao = escolha_operacao()
            if 1 <= operacao <= 4:
                tabuada(numero, operacao)
                break
            else:
                print('OPERADOR INVALIDO')
        except ValueError:
            print('Erro')
        except ZeroDivisionError:
            print('Não existe tabuada de zero')

validar_entradas()

while True:
    try:
        continuar = str(input('Gostaria de Ver outra Tabuada [S/N]:')).upper().strip()[0]
        if 'N' in continuar:
            break
        else:
             validar_entradas()
    except:
        print('VALOR INVALIDO DIGITE "S" OU "N"')