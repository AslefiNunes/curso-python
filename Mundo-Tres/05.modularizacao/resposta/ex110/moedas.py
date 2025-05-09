def aumentar(valor, aumen):
    valor = valor + (valor * (aumen / 100))
    return valor


def diminuir(valor, dimi):
    valor = valor - (valor * (dimi / 100))
    return valor


def dobro(valor):
    valor = valor * 2
    return valor


def metade(valor):
    valor = valor / 2
    return valor


def moeda(valor = 0, moeda ='R$', cond = False):
    if cond:
        return f'{moeda:>5}{valor:>.2f}'.replace('.',',')
    else:
        return valor
    
def linhas(msg = ''):
    largura = len(msg) + 15
    print('-'*largura)
    print(f'      {msg}')
    print('-'*largura)


def resumo(a=0,b=0, c=0):
    linhas('RESUMO DO VALOR')
    print(f'Preço analisado: {moeda(a,cond=True)}')
    print(f'Dobro do preco:  {moeda(dobro(a), cond=True)}')
    print(f'Metade do preco: {moeda(metade(a), cond=True)}')
    print(f'{b}% de aumento:  {moeda(aumentar(a,b),cond=True)}')
    print(f'{c}% de redução:  {moeda(diminuir(a,c),cond=True)}')
    print('-'*30)
    

