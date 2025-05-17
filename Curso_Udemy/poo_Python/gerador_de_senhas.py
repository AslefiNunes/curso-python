from random import randint
import string

senha = list()
teclado = (
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '@', '$', '!'
)

caracteres = string.ascii_lowercase
letra = string.ascii_letters # Maiuscula e Minuscula
letras_maiusculas = string.ascii_uppercase
numero = string.digits
caracteres  += string.punctuation

print(type(caracteres))
'''
while True:
    try:
        comprimento_senha = int(input('Com quantos caractes você quer a senha ? '))
        if 2 < comprimento_senha < 10:
            break
        else:
            print('Tente um valor entre 3 e 9 digitos')
    except:
        print('Valor Invalido tente novamente')

for i in range(0, comprimento_senha):
    senha.append(teclado[randint(0,len(teclado))])

print('A sua senha é : ', end='')

for i in senha:
    print(f'{i}', end='')

print('\nFim do Programa!')
'''