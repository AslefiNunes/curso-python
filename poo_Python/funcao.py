
def contador(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')
    if nome is not None:
        print(nome)
    else:
        print('Valor não encontrado')

list = [1,2,3,4,5]
contador(*list, nome = 'Aslefi', idade = 30)

n1, n2, *n = list

# função Lambda

lista = [
    ['p1',13],
    ['p2',25],
    ['p3',22],
    ['p4',10],
    ['p5',16]
]

#lista.sort(key=lambda item: item[1])
print(sorted(lista, key=lambda i: i[1]))

x = 10  #Aslefi
y = 'Aslefi' #10

x, y = y, x

print(f'x={x}  y={y}')