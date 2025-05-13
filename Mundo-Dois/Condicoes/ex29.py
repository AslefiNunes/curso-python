#Multa por velocidade 7 por km acima de 80 km/h

speed = float(input('Qual foi a velocidade do carro: '))
valor = 7
limite = 80

if speed > limite:
    #pago multa.
    m = (speed - limite) * valor
    print(f"você foi multado em R$ {m:.2f}")
else:
    print("Não foi multado")