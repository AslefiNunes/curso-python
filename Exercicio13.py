salario = float(input('Salario: '))
desconto = 0.15
aumento = salario * desconto

novo_salario = salario + aumento

print('O seu salario é R$ {:.2f} com 15% de aumento seu novo salario é R$ {:.2f}' .format(salario,novo_salario))