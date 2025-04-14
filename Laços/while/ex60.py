n = int(input('Escolha um numero e veja a sua fatoração: '))
fat = n
escolha = n
fatorando = f"{n}"
while n != 0:
    n -= 1
    if n != 0:
        fat = fat * n
        fatorando += f" x {n}"

print(f'{escolha}! {fatorando} = {fat}')
