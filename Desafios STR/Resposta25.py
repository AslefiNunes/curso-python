nome = str(input("Digite seu nome aquí: ")).strip().upper()

if "SILVA" in nome:
    #print("Seu nome tem Silva")
    print(f'Seu nome tem Silva na posição {nome.find("SILVA")}')
else:
    print("Seu nome não tem Silva")