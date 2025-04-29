tup = ("casa", "mesa", "livro", "azul", "verde", "sol", "lua", "flor")

for palavra in tup:
    print(f'\nNa palavra {palavra.upper()} temos', end =' ')
    for letras in palavra:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
    

'''tup = ("casa", "mesa", "livro", "azul", "verde", "sol", "lua", "flor")
vogais = 'aeiouAEIOU'
cont = 0

for palavra in tup:
    print(f'Na palavra {palavra} temos, ', end = '')
    for letra in palavra:        
        if letra in vogais:
            print(letra, end = ' ')
    print('\n')
    '''