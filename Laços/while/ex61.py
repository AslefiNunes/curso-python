n = int(input('Digite o primeiro termo: '))
p = int(input('Digite a razão: '))
decimo_termo = n + (10-1) * p

while True:
    print(n, end =" ")
    n += p
    if n == decimo_termo:
        print(n, end =" ")
        break
