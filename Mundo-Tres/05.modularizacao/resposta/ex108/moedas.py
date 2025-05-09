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


def moeda(valor = 0, moeda ='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')