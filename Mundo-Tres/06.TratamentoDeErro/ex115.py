from pratica import *

from time import sleep
while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até Logo')
        break
    else:
        print('\033[31mOpção invalida\033[m', flush=False)
    sleep(1)
