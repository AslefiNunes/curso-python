
def leiaDinhiero(frase = '', dinheiro = 0):
    while True:
        print(f'{frase}', end = '')
        dinheiro = str(input()).replace(',','.')
        if not dinheiro.isalpha() and dinheiro.strip == '':
            return float(dinheiro)
            break
        else:
            print(f'ERRO! O valor digitado {dinheiro} é invalido')
    
    