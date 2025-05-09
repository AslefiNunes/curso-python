c = ('\033[m)',       # 0 SEM - CORES
     '\033[0;30;41m', # 1 - VERMELHO
     '\033[0;30;44m'  # 2 - AZUL
     '\033[0;30;45m'  # 3 - Roxo
    ) 
     

def linhas(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end ='')
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)
    print(c[0], end='')

def sistemaHelp(acessar):
        help(acessar)

while True:
    linhas('SISTEMA DE AJUDA PyHELP', 2)
    respo = str(input('Função ou Biblioteca > ')).strip().lower()
    if respo == 'fim':
         break
    else:
         sistemaHelp(respo)

linhas('ATE LOGO!', 1)