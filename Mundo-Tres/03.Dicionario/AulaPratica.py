pessoas = {'nome':'Gustavo', 'idade':25, 'sexo':'M'}

print(pessoas)

print(pessoas['sexo'])

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)
pessoas['nome'] = 'Laandro'
del pessoas['idade']

for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['idade'] = 40

print(pessoas)

dicionario = dict()
lista = list()

for i in range(0,3):
    dicionario['cidade'] = str(input('Digite a cidade: '))
    dicionario['uf'] = str(input('Digite a Sigla do estado: '))
    lista.append(dicionario.copy())

print(lista)

for e in lista:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}')