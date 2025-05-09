def leiaInt(num=0):
    while True:
        num = str(input('Digite um número: ')).strip()
        if num.isnumeric():
            num = int(num)
            return num
            break
        else:
            print('ERRO! Digire um numero interio valido')

r = leiaInt()
print(r)