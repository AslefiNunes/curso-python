# Exercicio 67 - Tabuada com While

while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 20) 
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 20) 
    

print('Fim do programa !')