



'''n = (int(input('Digite um numero ')), int(input('Digite um numero ')), int(input('Digite um numero ')), int(input('Digite um numero ')))

print(f'O Valor 9 apareceu {n.count(9)} vezes')
print('Não possui valor 3' if 3 not in n else f'O numero 3 apareceu na {n.index(3) + 1}º')

for par in n:
    if par % 2 == 0: 
        print(par, end = ' ')'''

    
'''n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero: '))
    if 0 <= num <= 20:
        print(f'Você digitiou o numero {n[num]}')
        repit = str(input('Gostaria de continuar [S/N]: ')).strip().upper()[0]
        if repit == 'N':
            break
    else:
       print('Valor invalido digite novamente: ')
'''

'''times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Red Bull Bragantino', 'Ceara', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Juventude', 'Sao Paulo', 'Mirassol', 'Internacional', 'Bahia', 'Fortaleza', 'Botafogo', 'Vitória', 'Atletico Mineiro', 'Santos', 'Gremio', 'Sport Club do Recife')

print(times[:5])
print(times[-5:])
print(sorted(times))
time = times.index('Ceara') +1
print(time)'''

