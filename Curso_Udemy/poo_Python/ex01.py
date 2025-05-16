

def validar_Entrada():
    
    try: 
        nome = str(input('Digite seu nome: ')).strip()
        idade = int(input('Digite sua idade: '))
    except:
        print('Desculpe, você deixou campos vazios.')
    else:
        if len(nome) != 0:
            return nome, idade
        else:
            print('Desculpe, você deixou campos vazios.')


resposta = validar_Entrada()

if resposta is not None:
    print(f'Seu nome é {resposta[0]}')
    print(f'Seu nome invertido é {resposta[0][::-1]}')
    '''if '' in resposta[0]:
        print('Seu nome contem espaçõs vazios')
    else:
        print('Seu nome não contem espaçõs vazios')'''

    print('Seu nome contem espaçõs vazios') if ' ' in resposta[0] else print('Seu nome não contem espaçõs vazios')

    print(f'Seu nome tem {len(resposta[0])} letras')
    print(f'A primeira letra do seu nome é {resposta[0][0]}')
    print(f'A ultima letra do seu nome é {resposta[0][-1]}')
