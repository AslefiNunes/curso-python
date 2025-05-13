alunos = int(input('Digite o numero de alunos na sua turma: '))

nome = []
n1 = []
n2 = []
m = []


for i in range(alunos):
    print(f'{i + 1}º ALUNO')
    print(i)
    nome.append(str(input('Digite o nome do aluno: ').capitalize()))
    n1.append(float(input('Digite a primeira nota: ')))
    n2.append(float(input('Digite a segunda nota: ')))
    m.append((n1[i] + n2[i]) / 2)

print("MEDIA POR ALUNO")
print(20*'-')

for i in range(alunos):
    print(f'Aluno ª: {nome[i]:.2f} media: {m[i]:.2f}')

print(f'MEDIA GERAL: {sum(m) / alunos}')
print(20*'-')