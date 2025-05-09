from Livraria.arquivos import * 
from Livraria.interfac import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastraPessoa(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até Logo')
        break
    else:
        print('\033[31mOpção invalida\033[m', flush=False)
    sleep(1)
