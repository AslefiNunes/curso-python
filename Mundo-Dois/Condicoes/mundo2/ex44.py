import random
import time

print('Vamos jogar Jokenpô')

jogado = ['PEDRA', 'PAPEL', 'TESOURA']

jogar = str(input('Escolha entre, PEDRA, PAPAEL E TESOURA: ')).strip().upper()

cpu = random.choice(jogado)
time.sleep(0.5)
print("JO")
time.sleep(0.5)
print("KEN")    
time.sleep(0.5)
print("PÔ!!!")

if jogar == cpu:
    print(f'Empate')
elif jogar == "PAPEL" and cpu == "PEDRA" or jogar == "TESOURA" and cpu == "PAPEL" or jogar == "PEDRA" and cpu == "TESOURA":
    print(f'Você ganhou pois o computador escolheu {cpu}')
else:
    print(f'Você perdeu pois o computador escolheu {cpu}')