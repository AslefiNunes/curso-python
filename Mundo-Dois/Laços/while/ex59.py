from time import sleep

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
escolha = 0
 

while escolha != 5:
    print("""Escolha uma das opções abaixo:
    [1] Soma
    [2] Multiplicação
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa""")
    escolha = int(input("Digite sua opção: "))
    if escolha == 1:
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} = {soma}.")
    elif escolha == 2:
        mult = n1 * n2
        print(f"A multiplicação entre {n1} x {n2} = {mult}.")
    elif escolha == 3:
        if n1 == n2:
            print("Os números são iguais.")
        else:
            maior = max(n1, n2)
            print(f"Entre {n1} e {n2} O maior número é {maior}.")
    elif escolha == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    elif escolha == 5:
        print("Saindo do programa...")
        break
    else:
        print('Opção invalida tente novamente')
    sleep(1)
    print('=-=' * 10)

    