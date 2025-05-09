lista1 = []
lista2 = []

while True:
    lista1.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break

print(lista1)
# list2 = set(lista1) # cria uma nova lista apenas com valores que não se repetem 

#For cria uma lista com os itens que não se repetem 
for i in lista1:
    if i not in lista2:
        lista2.append(i)

#Printa a lista em ordem.
print(sorted(lista2))

