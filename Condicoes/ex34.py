# pergunta salario e determine o aumento maior que 1508 aumenta 10 menor aumetna 15%

salario = float(input('Qual o valor de seu Salario R$: '))

corte = 1508

if salario > corte:
    novo = salario * 0.1
else:
    novo = salario * 0.15

print(f'O aumento do seu salario é de R$ {novo:.2f} e o novo salario é de R$ {salario + novo:.2f}')