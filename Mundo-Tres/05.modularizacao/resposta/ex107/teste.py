import moedas 

p = float(input('Digite o preço R$ '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'A dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10% de {p} é {moedas.aumentar(p, 10)}')
print(f'Reduzindo 13%  de {p} é {moedas.diminuir(p, 13)}')