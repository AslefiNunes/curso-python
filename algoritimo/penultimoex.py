
#print(n *(n - 1))
#Exercício 1 - Faça um programa que leia o número de times e imprima todos os jogos possíveis entre eles.
'''
totTime = int(input("Digite o total de times: "))
times = []
jogos = totTime * (totTime - 1)


for i in range(totTime):
    times.append(str(input("Digite o nome do time: ")))

for i in range(totTime):
    for j in range(i + 1, totTime):
        print(f"{times[i]} x {times[j]}")
        print(f"{times[j]} x {times[i]}")  '''

#Exercicio 2 - Faça um programa que guarde um gabarito e verifiquei as notas dos alunos de acordo com o gabarito e qual a porcentagem de acertos. 

gabarito = []
alunos = []
notas = []
print('PASSO 1 - Total de Alunos e Questões')
total_alunos = int(input("Digite o total de alunos: "))
total_quest = int(input("Digite o total de questões do gabarito: "))

print('PASSO 2 - Cadastro de Gabarito')
print(20*"-")  
for i in range(total_quest):
    gabarito.append(str(input(f"Digite a resposta da questão {i + 1}: ")).lower())
while True:
    print(f'O Gabarito esta correto: {gabarito}')
    conf = str(input("O gabarito esta correto? [S/N]: ")).lower()
    if conf == 's':
        break
    else:
        gabarito.clear()
        for i in range(total_quest):
            gabarito.append(str(input(f"Digite a resposta da questão {i + 1}: ")).lower())

for i in range(total_alunos):
    nome = str(input('Qual o nome do aluno: '))
    alunos.append({"nome": nome, "respostas": [], "nota": 0})


#Exercico 3 - faça um programa que reserve espaçõs no cinema. 