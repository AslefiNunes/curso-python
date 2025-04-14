# leia grupo nome idade e sexo de 4 pessoas, mostra medida de idade, homen mais velho e nome, e quantas mulheres tem menos de 20 anos.

idade = []
nome = []
sexo = []
soma_idade = 0
h_velho = 0
nome_h_velho = ''
mulheres_menos_20 = 0

for i in range(0, 4):
    nome.append(str(input(f'Digite o nome da {i+1}ª pessoa: ')).strip())
    idade.append(int(input(f'Digite a idade da {i+1}ª pessoa: ')))
    sexo.append(str(input(f'Digite o sexo da {i+1}ª pessoa [M/F]: ')).strip().upper())
    soma_idade += idade[i]

for c in range(0, 4):
    if sexo[c] == 'M' and idade[c] > h_velho:
        h_velho = idade[c]
        nome_h_velho = nome[c]
    if sexo[c] == 'F' and idade[c] < 20:
        mulheres_menos_20 += 1


print(f'A media de idade do grupo é {soma_idade / 4} anos.')
print(f'O homem mais velho tem {h_velho} anos e se chama {nome_h_velho}.')
print(f'Ao todo são {mulheres_menos_20} mulheres com menos de 20 anos.')


# Resposta GUANABARA: 

