print(8 * "-=-")
print("Escola Santa Paciência")
print(8 * "-=-")
maior_nota = -1
aluno_destaque = ""

# Perguntar o número de alunos
aluno = int(input("Digite o número de alunos: "))

for i in range(1, aluno + 1):
    print(f"Aluno {i}")
    nome_aluno = str(input("Digite o nome do aluno: "))
    nota_aluno = float(input("Digite a nota do aluno: "))
    
    if nota_aluno > maior_nota:
        maior_nota = nota_aluno
        aluno_destaque = nome_aluno


print(f"O alunoª destaque é {aluno_destaque} com a nota {maior_nota}")