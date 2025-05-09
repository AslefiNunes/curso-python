
def escreva(frase):
    print('-'*len(frase))
    print(frase)
    print('-'*len(frase))


frase = str(input('Digite a frase: ')).upper().strip()
escreva(frase)
escreva('Olá, Mundo!')
