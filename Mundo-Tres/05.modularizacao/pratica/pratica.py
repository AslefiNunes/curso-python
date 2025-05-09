from pacot_uteis import numeros  # Criando pacotes com varios modulos.


num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobra(num)}')