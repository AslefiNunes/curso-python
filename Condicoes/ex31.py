#QUal a distancia da viagem em km calcular o preço da passagem  0,5 ate 200 km acima 0,45

dist = float(input('Qual a distancia em km: '))

pre1 = float(input('Qual o preço por km para viagens abaixo de 200 km de distancia: '))
pre2 = float(input('Qual o preço por km para viagens acima de 200 km: '))

if dist < 200:
    #valor = dist * pre1
    print(f'O preço da passagen é de R$ {dist * pre1:.2f}')
else:
    print('O preço da passagem é de R$ {:.2f}' .format(dist * pre2))