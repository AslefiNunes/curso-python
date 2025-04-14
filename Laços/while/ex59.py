n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: ")) 

print("""Escolha uma das opções abaixo:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos Números
[5] Sair do Programa""")

escolha = 0
 

while escolha != 5:
    escolha = int(input("Digite sua opção: "))
    if escolha == 1:
        soma = n1 + n2
        print(f"A soma é {soma}.")
    elif escolha == 2:
        mult = n1 * n2
        print(f"A multiplicação é {mult}.")
    elif escolha == 3:
        if n1 == n2:
            print("Os números são iguais.")
        elif n1 != n2:
            maior = max(n1, n2)
            print(f"O maior número é {maior}.")
    elif escolha == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    else:
        print("Saindo do programa...")
        break
    