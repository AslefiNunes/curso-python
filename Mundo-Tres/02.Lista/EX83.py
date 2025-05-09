'''valor1 = "("
valor2 = ")"
cont1 = 0
cont2 = 0
entrada = str(input('Digite a expressão: '))

for i in entrada:
    if valor1 == i:
        cont1 += 1
    elif valor2 == i:
        cont2 += 1

if cont1 == cont2:
    print('Sua formula esta correta: ')
elif cont1 > cont2:
    print('Você esqueceu de fechar o parentese')
elif cont1 < cont2:
    print('Você não abriu o parentese')'''

valore = str(input('Digite a expressão: '))
controle = list()

for simb in controle:
    if simb == '(':
        controle.append('(')
    elif simb == ')':
        if len(controle) > 0:
            controle.pop
        else:
            controle.append(')')

if len(controle) == 0:
    print('A expressão é valida')
else:
    print('Sua expressão não é valida ')