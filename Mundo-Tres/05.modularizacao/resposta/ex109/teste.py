import moedas 

p = float(input('Digite o preço: '))
formatac = str(input('Gostaria de ver Formatado [S/N]: ')).upper().strip()[0]
cond = True
if formatac == 'N':
    cond = False

print(f'A metade de {moedas.moeda(p, 'R$', cond)} é {moedas.metade(p, cond)}')
print(f'A dobro de {moedas.moeda(p, 'R$', cond)} é {moedas.dobro(p, cond)}')
print(f'Aumentando 10% de {moedas.moeda(p, 'R$', cond)} é {moedas.aumentar(p, 10, cond)}')
print(f'Reduzindo 13%  de {moedas.moeda(p, 'R$', cond)} é {moedas.diminuir(p, 13, cond)}')