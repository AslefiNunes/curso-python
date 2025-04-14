sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()

while not sexo == 'M' and not sexo == 'F':
    sexo = str(input('Dados inválidos. Por favor, Informe seu sexo: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso')

''''Minha resposta '
sexo = ' '
while True:
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()
    if sexo == 'M' :
        break
    elif sexo == 'F':
        break
    else:
        print('Dados inválidos. Por favor, informe apenas M ou F.')

print(f'Sexo {sexo} registrado com sucesso!')'''