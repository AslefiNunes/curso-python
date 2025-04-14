
valor = 0
soma = 0
media = 0
maior_num = 0
menor_num = 999
contador = 0

while True:
    valor = int(input('Digite o valor desejado: '))
    contador += 1
    soma += valor
    if valor >= maior_num:
        maior_num = valor
    if valor < menor_num:
        menor_num = valor
    if contador >= 2:
        media = soma / contador
        escolha = str(input('Gostaria de continuar Digitando valore [S/N]: ')).upper()
        if escolha == 'N':
            break


print(f'A Media dos valores digitados foi de {media} ')
print(f'O maior numero digitado foi de {maior_num}')
print(f'E O menor numero foi de {menor_num}')
