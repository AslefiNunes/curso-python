while True:
    print(17*"=")
    print("|      MENU     |")
    print(17*"=")
    print("| [1] De 1 a 10 |")
    print("| [2] De 10 a 1 |")
    print("| [3] PARA SAIR |")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        for i in range(1, 11):
            print(f"{i}...")
    elif escolha == 2:
        for i in range(10, 0, -1):
            print(f"{i}...")
    else:
        break
    