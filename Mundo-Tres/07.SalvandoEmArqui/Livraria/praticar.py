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
        print('Erro criação arquivo')
    else:
        print(f'Arquivo {arq} criado')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro de Leitura')
    else:
        print(a.read())
    finally:
        a.close()
        

def cadastraPessoa(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro no cadastro')
    else:
        try:
            a.write(f'{nome} {idade}anos\n')
        except:
            print('Erro ao escrever dados')
        else:
            print(f'Novo registro de {nome}')
if 19 % 2 == 0:
    print('Impa')
else:
    print('{}//{} = {}'.format(19,2,19//2))

n = 3*5+4**2

print(n)