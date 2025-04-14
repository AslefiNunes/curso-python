# computador pensar em um numero de 0 a 5 
import time 
import random

print("Estou pensado em um numero de 0 a 5 !")

print('PROCESSANDO...')
time.sleep(2)

n = [0, 1, 2, 3, 4, 5]

sort = random.choice(n)

escolha = int(input('Adivinhe qual o numero que o computador pensou: '))

if escolha == sort:
    print("Parabens você acertou")
else:
    print("Sinto muito eu pensei em {} e não em {} " .format(sort, escolha))


comp = random.randint(0, 5)