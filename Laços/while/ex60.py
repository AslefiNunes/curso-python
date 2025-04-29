n = int(input('Digite um numero para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! ', end = '')
while c > 0:
    f *= c
    print(f'{c}', end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    c -= 1

print(f)



''' Minha Resposta 

n = int(input('Escolha um numero e veja a sua fatoração: '))
fat = n
escolha = n
fatorando = f"{n}"
while n != 0:
    n -= 1
    if n != 0:
        fat = fat * n
        fatorando += f" x {n}"

print(f'{escolha}! {fatorando} = {fat}')'''
