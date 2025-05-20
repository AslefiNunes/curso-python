import os


palavra_secreta = 'PASSARO'
resposta = ['*' for i in range(len(palavra_secreta))]
cont = 0
print('Adivinhe a palavra: ', *resposta, end=' ')
print()

while True:
    try:
        escolher_letra = str(input('Escolha uma letra: ')).upper().strip()
        if not escolher_letra.isalpha():
            print('ERRO: Digite apenas letras')
            continue 
        elif len(escolher_letra) != 1:
            print('ERRO: Digite apenas uma letra')
            continue 
        elif escolher_letra in resposta:
            print('ERRO: Você já escolheu essa letra')
            continue
        cont += 1
        for i, v in enumerate(palavra_secreta):
            if escolher_letra == v:
                resposta[i] =  v
        print(*resposta, end=' ')
        print()
        if resposta == list(palavra_secreta):
            print('Você acertou a palavra')
            break
    except Exception as e:
        print(f'ERRO: Não tratado {e}')
        
os.system('cls')
print('PARABENS VOCÊ GANHOU')
print(f'Você tentou {cont} vezes e a palavra era {palavra_secreta}')
print('FIM DO JOGO')

        