#Calcular preço do produto de acordo com a condição de pagamento.

forma = int(input('Escolha a forma de pagamento:\n'
    '	1 - Dinheiro ou Cheque 10% de desconto\n'
    '	2 - Cartão a vista 5% de desconto\n'
    '	3 - 2x no Cartão sem desconto\n'
    '	4 - 3x ou mais 20% de juros\n'
    'Escolha uma das opções: '))

produto = float(input('Digite o valor do produto: R$ '))

dinheiro = 0.1
cart_avist = 0.05
cart_parce = 0.2

if forma == 1:
	produto = produto - ( produto * dinheiro)
elif forma == 2:
	produto = produto - (produto * cart_avist)
elif forma == 3:
	produto = produto 
else:
	produto = produto + (produto * cart_parce)

print(f'O valor do produto é de R$ {produto:.2f}')