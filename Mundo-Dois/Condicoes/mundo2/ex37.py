op = int(input('Digite um número real inteiro: '))
print('Escolha uma das opções abaixo:')
print('1 - Binario')
print('2 - Octal')
print('3 - Hexadecimal')  
n = int(input('Qual a opção desejada: '))

if n == 1: 
    print(f'O número {op} em binário é {bin(op)[2:]}')
elif n == 2:
    print(f'O número {op} em octal é {oct(op)[2:]}')
elif n == 3:
    print(f'O número {op} em hexadecimal é {hex(op)[2:]}')