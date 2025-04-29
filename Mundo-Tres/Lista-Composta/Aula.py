galera = [['Aslefi', 31], ['Ellen', 26], ['Soffia', 10], ['Celia', 55], ['Antonio', 68]]
dados = []

print(galera[2])
print(galera[2][0])

for i in galera:
    print(i[0])

for i in galera:
    print(i[1])

for p in galera:
    print(f'{p[0]} tem {p[1]} idade')

#Part 2

galera = []
dados = []
maior18 = 0
menor18 = 0

for c in range(0,3):
    dados.append(str(input('Digite nome: ')))
    dados.append(int(input('Qual a idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} tem mais de 18 anos')
        maior18 += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor18 += 1

print(f'Temos {maior18} pessoas maiores de 18 anos de idade')
print(f'Temos {menor18} pessoas menores de 18 anos')