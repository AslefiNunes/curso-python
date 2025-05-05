def soma (a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

soma(5, 3)
soma(4, 5)
soma(b = 4, a=5)


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam}')


contador(5, 3)
contador(4, 5, 3)
contador(1, 5, 3, 2)

valores = [7, 4, 5, 3, 2]

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


dobra(valores)
print(valores)

def somando(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é igual a {s}')


somando(5, 3, 4, 6)
somando(5, 2)