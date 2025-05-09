'''help(print)

print(print.__doc__)

def contador(i,f,p):
    """
    ->Faz uma contagem e mostra na tela:
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Aslefi Nunes - Trainer 
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')
contador(2,10,2)
help(contador)'''





def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'o valor de a local é {a}')
    print(f'o valor de b local é {b}')
    print(f'o valor de c local é {c}')


a = 5
teste(a)
print(f'O valor de a global é {a}')

def soma(a=0,b=0,c=0):
    s = a +b + c
    return s

r1 = soma(4,2,10)
r2 = soma(4,2)
r3 = soma(2,10)

print(f'As somas são {r1}, {r2}, {r3}')



help(int)