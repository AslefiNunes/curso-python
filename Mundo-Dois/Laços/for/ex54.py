# Ler ano de nascimento de 7 pessoas, no final mostra quantas pessoas maiores de 21 anos. 
ano_calendario = int(input('Informe qual o ano atual ou ano que voce quer saber a idade:'))
ano_nacido = []
tamanho_grupo = int(input('Informe quantas pessoas deseja analisar: '))

maior_de_idade = 0

for i in range(0, tamanho_grupo):
    ano_nacido.append(int(input(f'Digite o ano de nascimento da {i+1}ª pessoa: ')))
    if ano_calendario - ano_nacido[i] >= 21:
        maior_de_idade += 1

print(f'No total {maior_de_idade} pessoas são maiores de 21 anos!')
print(f'No total {tamanho_grupo - maior_de_idade} pessoas são menores de 21 anos!')