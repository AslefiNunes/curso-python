num = []

while True:
    num.append(int(input('Digite o valor desejado: ')))
    if len(num) > 5:
        perg = str(input('Gostaria de Para [S/N]: ')).strip().upper()[0]
        if perg == 'S':
            break


print(f'foram digitados {len(num)} numeros')
num.sort(reverse=True)
print(f'A lista decresente é {num}')
print('O valor 5 na lista' if 5 in num else 'O valor 5 não foi encontrado')