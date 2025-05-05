'''people = list()

cadastro = {}
soma = media = 0

while True:
    cadastro['nome'] = str(input('Digite o nome: '))
    cadastro['sexo'] = str(input('Digite o sexo [F/M]: ')).upper().strip()[0]
    cadastro['idade'] =  int(input('Qual a idade: '))
    soma += cadastro['idade']
    people.append(cadastro.copy())
    parar = str(input('Gostaria de para [S/N]: ')).upper().strip()[0]
    if 'S' in parar:
        break


print(f'O grupo tem {len(people)} pessoas. ')
for i in people:
    for k, v in i.items():
        if k == 'idade':
            somaIdade += v
                
media = somaIdade / len(people)

print(f'A media de é {media} anos de idade')


print('As mulheres cadastradas foram: ', end = ' ')
for i in people:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}', end ='')
    print()
print('Lista das pessoas com idade acima da media', end = ' ')
for i in people:
    if i['idade'] > media:
        print('   ')
        for k, v in i.items():
            print(f'{k} = {v}', end = ' ')
        #print(f'nome = {i["nome"]}, sexo = {i["sexo"]} idade = {i["idade"]}')
        print()

print('Fim do Program')


'''
'''grupo = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas['nome'] = str(input('Digite o nome: '))
    pessoas['sexo'] = str(input('Digite o Sexo [F/M] '))
    pessoas['idade'] = int(input('Qual a idade: '))
    soma += pessoas['idade']
    grupo.append(pessoas.copy())
    para = str(input('PARA [S/N] '))[0]

    if para in 'Ss':
        break'''

grupo = [{'nome': 'Aslefi', 'sexo': 'M', 'idade':31 }, {'nome': 'Ellen', 'sexo': 'F', 'idade': 26}, {'nome': 'Soffia' , 'sexo': 'F', 'idade': 12}, {'nome': 'Joice', 'sexo': 'F', 'idade':54 }]

soma = media = 0
print(grupo)

for i, v in enumerate(grupo):
    if v['idade']:
        soma += v['idade']

print(f'A) O grupo tem {len(grupo)} pessoas. ')
media = soma / len(grupo)
print(f'B) A média de idade é {media}')

print('As mulheres cadastradas foram: ', end='')

for i, v in enumerate(grupo):
    if v['sexo'] in 'F':
        print(f'{v["nome"]},', end = ' ')
print()

print('Lista das pessoas a cima da média: ')

for i in grupo:
    if i['idade'] > media:
        for k, v in i.items():
            print(f'{k} = {v} ', end = ' ')