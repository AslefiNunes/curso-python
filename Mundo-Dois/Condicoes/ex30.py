#leia um numero inteiro e identifique se ele é par4

number = int(input('Digiti um numero real interio: '))

if number % 2 == 0:
    print(f'O numero {number} é Par')
else:
    print('O numero {} é IMPAR' .format(number))