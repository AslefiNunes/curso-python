nome = "Aslefi"
cores = {
    'limpa': '\033[m',
    'azul': '\033[1;34m',
    'amarelo': '\033[1;33m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'branco': '\033[1;37m',}

print('Olá, {}{}{}' .format(cores['azul'],nome,cores['limpa']))

print(f' {nome} que nome {cores["verde"]} Bonito!{cores["limpa"]}')