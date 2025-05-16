'''nome = 'Luis Otario'

cont = 0
while cont < len(nome):
    print(f'*{nome[cont]}', end = '')
    cont += 1
print('*')'''

# Crie uma calculadora com While - pergunto ao usuario 2 valores primeir é denominador peça tbm a operação que vai ser +, -, *, /

n1 = 1
while True:
        try:
            n2 = int(input('Digite qual a tabuda você que ver: '))
            operador = int(input('Escolha uma das opeções:\n' \
            '[1] - Adição\n' \
            '[2] - Subitração\n' \
            '[3] - Multiplicação\n' \
            '[4] - Divisão\n ' \
            'Faça sua Escolha: '))
        except:
            print('VALORES INVALIDOS TENTE NOVAMENTE')
        else:
            if operador > 4:
                print('OPERADOR INVALIDO')
            else:
                break

while n1 <= 10:
    if operador == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif operador == 2:
        print(f'{n1} - {n2} = {n1-n2}')
    elif operador == 3:
        print(f'{n1} x {n2} = {n1*n2}')
    else:
        print(f'{n1} / {n2} = {n1/n2}')
    n1 += 1