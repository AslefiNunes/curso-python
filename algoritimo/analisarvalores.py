quantidade = int(input("Quantos números você deseja digitar? "))

i = 1
cont = 0
divs = 0
nul = 0
somaPar = 0

while i <= quantidade:
    n = int(input(f'Digite o {i}º numero: '))
    i += 1
    cont = cont + n
    if n % 5 == 0:
        divs += 1
    if n == 0:
        nul += 1
    if n % 2 == 0:
        somaPar = somaPar + n


print("A soma dos numeros digitados é:", cont)
print("A media dos numero digitados é {:.2f}" .format(cont/(i - 1)))
print(f"A quantidade de numeros divisiveis por 5 é: {divs}")
print("A quantidade de numeros nulos é:", nul)
print("A soma dos numeros pares é:", somaPar)
