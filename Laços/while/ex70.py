total = totmil = menor = cont = 0
while True:
    produto = str(input('Qual o nome do produto: '))
    preco = int(input('Qual o valor do item R$: '))
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        menor = preco
        baratinho = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Gostaria de finalizar o programa? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('{:-^40}' .format('FIM DO PROGRAMA'))
print(f'O total gasto foi de R$ {total:.2f}')
print(f'Temos {totmil} produtos que custam mais de R$ 1.000,00')
print(f'O produto mais barato {baratinho} e custa R$ {menor:.2f}')

''' Resposta Aslefi

print('=' * 30)
print('Lista de compras')
cust_benef = total = primiun = baratinho = contador = 0

while True:
    contador += 1
    print('=' * 30 )
    produto = str(input('Qual o nome do produto: '))
    preco = int(input('Qual o valor do item: '))
    print('=' * 30 )
    total += preco
    if preco > 1000: 
        primiun += 1
    if contador == 1 :
        baratinho = produto
        cust_benef = preco
    else:
        if preco < cust_benef:
            baratinho = produto
            cust_benef = preco
    fim = str(input('Gostaria de finalizar o programa? [S/N]')).upper().strip()
    if fim == 'S':
        break
    
print(f'A) O total gasto foi de\033[1;31m R$ {total:.2f}\033[m\nB)\033[1;31m {primiun}\033[m Produtos valem mais de\033[1;31m  R$ 1.000,00\033[m')

if contador < 2:
    print(f'C) Teve apenas \033[1;32m 1,00 \033[m item cadastrado e ele vale  \033[1;32m R$ {cust_benef:.2f}\033[m ')
else:
    print(f'C)\033[1;32m {baratinho} \033[m foi o mais barato e vale \033[1;32m R$ {cust_benef:.2f}\033[m')'''

