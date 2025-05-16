'''def checar_num_inteiro():
    try:
        numero = int(input('Digite um numero inteiro: '))
    except(ValueError):
        print('O valor digitado não é um numero inteiro')
    except(TypeError):
        print('DADOS INVALIDOS')
    else:
        return numero
    
resposta = checar_num_inteiro()

if resposta is not None:
    if resposta % 2 == 0:
        print(f'O valor {resposta} é PAR')
    else:
        print(f'O valor é {resposta} IMPAR')'''
'''def validar_numero():
    try:
        horas = int(input('Digite apenas as horas: '))
        if horas >= 0 and horas <= 11:
            print('Bom dia')
        elif horas >= 12 and horas <= 17:
            print('Boa tarde')
        elif horas >= 18 and horas <= 23:
            print('Boa noite')
        else:
            print(f'Este valor é invalido')
    except:
        print('Valor invalido')
    
validar_numero()'''
'''nome_curto = 4
nome_medio = 6
nome_grande = 7

def medir_nome():
    try:
        seu_nome = str(input('Digite seu primeiro nome: '))
    except:
        print('ERRO: O valor digitado é invalido.')
    else:
        if len(seu_nome) <= nome_curto:
            print('Seu nome é curto')
        elif len(seu_nome) <= nome_medio:
            print('Seu nome é normal')
        else:
            print('Seu nome é grande')

medir_nome()'''