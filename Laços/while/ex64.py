
num = 0
soma = 0
contador = 0

while num != 999:
    num = int(input('Digite um numero interio de 0 a 998 ao digitar 999 o programa finaliza: '))
    contador += 1
    soma += num
    

print(f'O total de numeros digitados foi de {contador - 1}')
print(f'O total de numeros digitados foi de {soma - 999}')
