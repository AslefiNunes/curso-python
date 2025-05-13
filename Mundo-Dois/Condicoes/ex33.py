#Leia tres numero e verificar qual é o maio e menor
n = []

for i in range(3):
    n.append(int(input(f'Digite o {i + 1}º: ')))

print(f'O maior numero é {max(n)}')

print(f'E o menor valor é {min(n)}')
