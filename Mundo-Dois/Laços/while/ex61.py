n = int(input('Digite o primeiro termo: '))
p = int(input('Digite a razão: '))
decimo_termo = 1

while decimo_termo <= 10:
    print(n, end =" ")
    n += p
    decimo_termo +=1

print('FIM...')