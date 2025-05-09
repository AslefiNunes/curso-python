def fatorial(num, show):
    """
    ->Calculando o Fatorial de um número.
    :param num: O numero a ser calculado.
    :param show: (opcional) Mostrar os não a conta.
    :return: O valor do Fatorial de um número n.    
    """
    fator = 1
    while num > 0:
        fator *= num
        if show:
            print(f'{num} x ', end = '' ) if num != 1 else print(f'{num} = ', end ='')
        num -= 1
        
    return fator
    
fat = int(input('Qual numero deseja ver o fatorial: '))
cond = str(input('Gostaria de ver a fatoração [S/N]: ')).upper().strip()[0]

if cond in 'S':
    show = True
else:
    show = False
    
print(f'{fatorial(fat, show)}')

help(fatorial)