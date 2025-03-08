numero_binario = input('Digite um numero binario qualquer: ')

numero_decimal = 0
expoente = 0
resultado = 0

for digito in reversed(numero_binario):
    numero_decimal = int(digito) * 2 ** expoente
    expoente += 1
    resultado += numero_decimal



print('O Numero Binario {}, corresponde ao numero decimal {}' .format(numero_binario, resultado))
