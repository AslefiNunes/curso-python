import random
n1 = str(input('Primeiro Nome: '))
n2 = str(input('Segundo Nome: '))
n3 = str(input('Terceiro Nome: '))
n4 = str(input('Quarto Nome: '))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print('O Aluno escolhido foi {}' .format(escolhido))