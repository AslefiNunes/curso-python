tabela = ('Lápis', 1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Tranferidor', 4.20,'Compaso',9.99,'Mochila',120.32)

'''
for i in range(0, len(tabela), 2):
    nome = tabela[i]
    valor = tabela[i+1]
    print(f'{nome:.<30} R$ {valor:.2f}')
'''

for pos in range(0, len(tabela)):
    if pos % 2 == 0:
        print(f'{tabela[pos]:.<30}', end = ' ')
    else:
        print(f'R$ {tabela[pos]:.2f}')