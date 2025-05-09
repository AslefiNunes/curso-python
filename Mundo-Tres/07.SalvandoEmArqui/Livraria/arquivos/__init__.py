from Livraria.interfac import cabecalho


def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um Erro na criação do arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastraPessoa(arq, nome='desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abri arquivo para cadastro')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao adicionar pessoa no arquivo')
        else:
            print(f'{nome} adicionado ao arquivo')
            a.close()
