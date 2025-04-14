tri = []
def metodo():
    for i in range(3):
        tri.append(int(input(f'Digite o valor do {i + 1}º segmento de reta: ')))
        if i == 2:
            a = tri[0]
            b = tri[1]  
            c = tri[2]

    if a + b > c and a + c > b and b + c > a:
        print('Os segmentos acima PODEM FORMAR um triângulo')
        if a == b == c:
            print('EQUILÁTERO')
        elif a != b != c != a:
            print('ESCALENO')
        else:
            print('ISÓCELES')
    else:
        print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

while True:
    metodo()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break