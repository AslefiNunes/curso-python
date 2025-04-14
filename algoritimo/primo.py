n = int(input('Digite um número : '))
c = 1
contd = 0

while not c > n:
    if n % c == 0:
        contd = contd + 1
    c = c + 1

if contd == 2:
    print(f'O número {n} é ')
else:
    print(f'O número {n} não é')
    

