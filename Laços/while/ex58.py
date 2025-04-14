''' Resposta do Gustavo'''

'''
from time import sleep
from random import randint

computador = randint(0, 10)
print('Sou seu COMPUTADOR... Acabei de pensar em um número entre 0 e 10.')
print('Sera que você consegue adivinhar qual foi ? ')
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite ? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente novamente')
        elif jogador > computador:
            print('Menos... Tente novamente')

print(f'Parabens voce acrtou na {palpites}º tentativa')


 Minha Resposta'''
import time 
import random

contador = 0

print("Estou pensado em um numero de 0 a 10 !")

print('PROCESSANDO...')
time.sleep(2)

n = [0, 1, 2, 3, 4, 5,6,7,8,9,10]

sort = random.choice(n)

while True: 
    escolha = int(input('Adivinhe qual o numero que o computador pensou: '))
    contador += 1
    if escolha != sort:        
        print("Tente novamente")
    else:
        print("Parabens você acertou")
        break

print("Você tentou {} vezes".format(contador))