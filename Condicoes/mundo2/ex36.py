# emprestimo mobiliario

salario = float(input('Qual o seu salario? R$  '))
quant_parc = int(input('Qual a quantidade de parcelas: '))
valor_casa = float(input('Qual o valor da casa? R$  '))

anos = quant_parc / 12
parcela = valor_casa / quant_parc
limite = salario * 0.3

if parcela < limite:
    print('Emprestimo aprovado! O valor da sua parcela é de R$ {:.2f}'.format(parcela))
    print(f'O Seu finacimanto vai durar {anos:.0f} anos')
else:
    print('Emprestimo negado! O valor da sua parcela é de R$ {:.2f}'.format(parcela))
    print('O valor máximo da parcela é de R$ {:.2f}'.format(limite))