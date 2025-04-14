nome = str(input('Digite seu nome completo: ')).strip().upper()

respost = nome.split()
print(len(respost))
print('Seu primeiro nome é: {}' .format(respost[0]))
print('Seu último nome é: {}' .format(respost[len(respost)-1]))

print(respost)

