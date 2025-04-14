# tres medidas de reta para verificar se pode ser um triangulo para que seja verdadero a soma de 2 dos lados tem que ser maior que o 3 lado 

tri = []
a, b, c = 0, 0, 0
for i in range(3):
    tri.append(int(input(f'Digite o {i + 1}º do triangulo: ')))
    if i == 2:
        a = tri[0]
        b = tri[1]
        c = tri[2]

if a + b > c and  a + c > b and b + c > a:
    print('As retas formaram um triangulo:')
    if a == b == c:
        print('Triângulo Equilátero')
    elif a != b != c:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else: 
    print('Não é possivel gerar um triangulo com os valores informados')

# Resposta da aula!

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')
