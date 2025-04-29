lista1 = []
valor  = 0

for i in range(0, 4):
    valor =  int(input('Digite um numero: '))
    if i == 0:
        lista1.append(valor)
    else:
        if valor > lista1[0]:
            lista1.insert(i, valor)
        else:
            lista1.insert(0, valor)
        
    
print(lista1)