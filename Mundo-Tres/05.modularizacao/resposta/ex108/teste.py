import moedas 

p = float(input('Digite o preço R$ '))
print(f'A metade de {moedas.moeda(p,'u$')} é {moedas.moeda(moedas.metade(p),'U$')}')
print(f'A dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando 10% de {p} é {moedas.aumentar(p, 10)}')
print(f'Reduzindo 13%  de {p} é {moedas.diminuir(p, 13)}')