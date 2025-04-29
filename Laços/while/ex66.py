soma = 0
contador = 0

while True:    
    n = int(input('Digite um valor sendo 999 condição de parada '))
    if n == 999:
        break
    else:
        soma += n
        contador += 1
        

print(f'Foram digitados {contador} numeros e sua soma é {soma}')