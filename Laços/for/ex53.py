#LEia uma frase qualquer e verifica se é um palíndromo. - APOS A SOPA leia de tras pra frente. 

frase = str(input('Digite uma frase: ')).strip().upper()

tirar_espaco = frase.replace(" ", "")

inverso = tirar_espaco[::-1]

print(f'frase {tirar_espaco} seu inverso {inverso}')
if tirar_espaco == inverso:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

'''
inverso_do_for = ''

for letra in range(len(tirar_espaco) -1, -1, -1):
    inverso_do_for += tirar_espaco[letra]
print(inverso_do_for)
'''