'''while True:


    try:#OPERAÇÃO
        num = int(input('Numerador: '))
        dem = int(input('Denominador: '))
        resul = num / dem
    except Exception as erro:#FALHO
        print(F'Erro, problema encontrado foi {erro.__class__}')
    except(ValueError):
        print('Erro de Valor')
    else:# CERTO
        print(f'O resultado da divisão é {resul}')
    finally:#CERTO OU ERRADO '''
from time import sleep

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[033mErro!\033[m digite uma opção valida.')
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario.')
            return 0
        else:
            return num


def linha(tam = 40):
    print('-'*tam)


def cabecalho(text):
    linha()
    print(text.center(40))
    linha()

def menu(txt):
    linha()
    print('MENU PRINCIPAL'.center(40))
    linha()
    cont = 1
    for i in txt:
        print(f'\033[33m{cont}\033[m - \033[34m{i}\033[m')
        cont += 1
    linha()
    opc = leiaInt('Sua Opção: ')
    return opc