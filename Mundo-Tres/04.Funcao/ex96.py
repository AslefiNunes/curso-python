def traco():
    print('-'*20)

print('Controle de Terrenos')
traco()

largura = float(input('LARGURA(m): '))
altura = float(input('ALTURA(m): '))
traco()

def area(larg, alt):
    result = larg * alt
    print(f'A área de um terreno {larg:.2f} x {alt:.2f} é de {result:.2f} m².')

area(largura, altura)
