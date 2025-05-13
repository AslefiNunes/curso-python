tot18 = totH = totF = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totF += 1
    resp = ' ' 
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totF} mulheres com menos de 20 anos')
''' respota ASLEFI


idade = 0 
Sexo = ''
maior_idade = mulheres = homens = 0

print('*' * 20 )
print('Cadastro de pessoas')
print('*' * 20 )

while True:
    print('=' * 20)
    sexo = str(input('Qual o genero: ')).strip().upper()
    idade = int(input('Qual a idade: '))
    print('=' * 20)
    if sexo not in ('H', 'M') and idade < 0:
        print('Dados Invalidos, tente novamente: ')
    else:
        if idade > 18:
            maior_idade +=1
        if sexo == 'M' and idade < 20:
            mulheres += 1
        elif sexo == 'H':
            homens += 1
        continuar = str(input('Gostaria de continuar: [S/N]')).strip().upper()
        if continuar == 'N':
            break
        

print(f' A) {maior_idade} pessoas tem mais de 18 anos \n B) {homens} homens foram cadastrados \n C) {mulheres} mulheres com menos de 20 anos foram cadastradas no sistema')'''