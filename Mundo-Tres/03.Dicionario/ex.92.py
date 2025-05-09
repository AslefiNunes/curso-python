func = dict()

aposentarIdade = 65
anosContribui = 35
aposentarContriu = 0

anoAtual = int(input('Qual o ano que você que considerar como atual: '))
nomeFunc = str(input('Digite o nome do Funcionario: '))
anoNasci = int(input('Digite o ano que ele nasceu: '))

idade = anoAtual - anoNasci
aposentar = aposentarIdade - idade

func['nome'] = nomeFunc
func['idade'] = idade


ctps = int(input('Carteira de Trabalho (0 não tem): '))

if ctps != 0:
    func['ctps'] = ctps
    anoContrato = int(input('Digite ano do contrato: '))
    func['contratação'] = anoContrato
    aposentarContriu = anoAtual - anoContrato
    func['aposentadoria'] = idade + (anosContribui - aposentarContriu)
    print('-=-'*15)
    for k, v in func.items():
            print(f'{k} tem valor {v}')

else:
    print('-=-'*15)
    for k, v in func.items():
        print(f'{k} tem valor {v}')
    print( f'{func["nome"]} vai aposentar por idade com 65 anos e falta {aposentar} anos para aposentar')


print('-=-'*15)
print(func)
