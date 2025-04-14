# soma se numeroes impares e multiplos de 3 -divisivel por 3 - entre 1 e 500
soma = 0

for i in range(1, 501 , 2):
    if i % 3 == 0:
        soma = soma + i

print(f'O total da soma dos numeros impares e multiplos de  3 é de {soma}')