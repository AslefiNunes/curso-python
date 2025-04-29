contador = 0
soma = 0

while True:
    escolha = int(input('Digite um valor para solar se digitar 999 finaliza o programa: '))
    if escolha != 999:
        soma += escolha
        contador += 1
    else:
        break


print(f'O total de numeros digitados foi de {contador} e sua soma é {soma}')
'''escolha = 0
soma = 0
contador = 0

while escolha != 999:
    escolha = int(input('Digite um numero interio de 0 a 998 ao digitar 999 o programa finaliza: '))
    if escolha != 999:
        contador += 1
        soma += escolha
    
    

print(f'O total de numeros digitados foi de {contador}')
print(f'A Soma dos dos numeros digitados foi de {soma}')'''
