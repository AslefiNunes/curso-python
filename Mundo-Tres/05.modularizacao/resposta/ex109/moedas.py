def aumentar(valor, aumen, format):
    res = valor + (valor * (aumen / 100))
    return res if format is False else moeda(res,cond=format)


def diminuir(valor, dimi, format):
    res = valor - (valor * (dimi / 100))
    return res if format is False else moeda(res,cond=format)


def dobro(valor, format):
    res = valor * 2
    return res if format is False else moeda(res,cond=format)


def metade(valor, format):
    res = valor / 2
    return res if format is False else moeda(res,cond=format)


def moeda(valor = 0, sif ='R$', cond = False):
    if cond:
        return f'{sif}{valor:.2f}'.replace('.',',')
    else:
        return valor