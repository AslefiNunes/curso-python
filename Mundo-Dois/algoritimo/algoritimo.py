l1, l2, l3 = int(input('Digite o valor do primeiro lado: ')), int(input('Digite o valor do segundo lado: ')), int(input('Digite o valor do terceiro lado: '))

eq = (l1 == l2) and (l2 == l3)

es = (l1 != l2) and (l2 != l3) and (l1 != l3)
tri = (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2)

if tri:
    if eq:
        print('O triangulo é Equilátero')
    else:
        if es:
            print('O triangulo é Escaleno')
        else:
            print('O triangulo é Isósceles')
else:
    print('Os valores informados não formam um triangulo')