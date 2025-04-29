escola = []
while True:
    aluno = str(input('Digite o nome do aluno:' ))
    nota1 = float(input('Digite a primeira nota: '))
    nota2  = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    escola.append([[aluno],[nota1,nota1], [media]])
    
    cont = str(input('Gostaria de Continuar[S/N]: ')).upper().strip()[0]
    if 'N' in cont:
        break

print(escola)
cont = 0
print(f'{"No.":<6}{"NOME":<8}{"MEDIA":>8}')

for i, v in enumerate(escola):
    print(f'{i:<6}{v[0]:<8}{v[2]:>8.1f}')

while True:
    cont += 1
    if cont < 3:
        opc = int(input('Digite o "No." do aluno para ver suas notas: '))
        print(f'{escola[opc][0]} suas notas foram {escola[opc][1]} ')
    else:
        break