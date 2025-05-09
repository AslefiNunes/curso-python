dias = int(input('Digite quantidade de dias alugado: '))
km = float(input('Digite quantidade de KM: '))

custo_dia = dias * 60
custo_km = km * 0.15

custo_total = custo_dia + custo_km

print('O valor do aluguel do carro foi de R$ {:.2f}' .format(custo_total))