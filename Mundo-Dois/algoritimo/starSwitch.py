

soC = []
tot = 0

while True:
    try:
        nomes = int(input("Quantos nomes você quer adicionar? "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro.")

while True:
    letra = str(input("Digite uma letra: ")).capitalize()
    if len(letra) == 1 and letra.isalpha():
        break
    else:
        print("Por favor, digite apenas uma letra.")

for i in range(nomes):
    n = str(input(f"Digite o {i + 1}º nome: ")).capitalize()
    if n.startswith(letra):
        soC.append(n)
        tot += 1
    

print(f'O total de nomes que começam com a letra {letra} é: {tot}')

for i in range(tot):
    print({soC[i]})
