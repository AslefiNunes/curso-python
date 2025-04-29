n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Digite um número: '))
    if escolha < 0 or escolha > 20:
        print('Número inválido. Tente novamente.')
    else:
        print(f'Você digitou o número {n[escolha]}')   
        break

print('Fim do programa !')