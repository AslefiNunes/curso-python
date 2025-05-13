inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))

if inicio < fim:
    while inicio < fim +1:
        print(inicio)
        inicio += 1
else:
    while inicio > fim -1:
        print(inicio)
        inicio -= 1
        

if inicio > fim:
   for i in range(inicio, fim - 1, -1):
       print(f"{i}...")
else:
    for i in range(inicio, fim + 1):
        print(f"{i}...")