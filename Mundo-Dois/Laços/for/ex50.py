# ler 6 numeros e se par soma se impar desconsidera.

num = []
soma = 0

for i in range(0, 6):
    num.append(int(input(f'Digite o {i + 1}º numero: ')))

for i in range(0, 6):
    if num[i] % 2 == 0:
        soma = soma + num[i]

print(f'A soma dos numeros pares foi de {soma}')