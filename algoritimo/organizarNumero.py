vetor = []

i, j, aux = 0, 0, 0

for i in range(4):
    vetor.append(int(input("Digite um número: ")))

for i in range(3):
    for j in range(i + 1, 4):
        if vetor[i] > vetor[j]:
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux
print("Os números em ordem crescente são:")
for i in range(4):
    print(vetor[i])

