# Leia pesso e mostre maio e menor pesso, usar laço e lista.

peso = []

for i in range(0, 5):
    peso.append(float(input(f'Digite o peso da {i+1}ª pessoa: ')))

print(f'O maior peso é {max(peso)} e o menor peso é {min(peso)}')

