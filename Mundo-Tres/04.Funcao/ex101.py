anoAtual = 2025

def voto(ano):
    from time import sleep # IMPORTAR BIBLIOT DENTRO DA FUNC ECONOMIZA MEMORIA. 
    idade = anoAtual - ano
    print(f'Com {idade} anos: VOTO ', end = '') 
    if idade >= 18:
        if idade < 65:
            return 'OBRIGATORIO'
        else:
            return 'OPCIONAL'
    else:
        return 'NEGADO'
       
anoNasce = int(input(f'Em que ano você nasceu: '))
print(voto(anoNasce))