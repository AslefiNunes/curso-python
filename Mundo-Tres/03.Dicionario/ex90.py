'''turma = dict()

turma['nome'] = str(input('Digite o nome do aluno: '))
turma['media'] = int(input('Digite a media do aluno: '))
turma['condicao'] = 7

for k, v in turma.items():
    if k != 'condicao':
        print(f'{k} é igual a {v}')
    else:
        if turma['media'] >= turma['condicao']:
            print('Situação igual Aprovado')
        else:
            print('Situa igual a Reprovado')'''


aluno = {}

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a media do aluno: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'

print('-='*29)
for k, v in aluno.items():
    print(f'{k} é igual {v}')