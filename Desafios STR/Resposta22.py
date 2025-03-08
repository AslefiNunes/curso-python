from time import sleep 

nome = str(input('Digite seu nome: ')).strip()
print("Analisando seu nome...")
sleep(2)
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome)} letras")
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
print(f"Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras")
print(f"Seu ultimo nome é {nome.split()[-1]} e ele tem {len(nome.split()[-1])} letras")