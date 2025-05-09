''' Em ordem de precedencia Dos operadores Aritimeticos 
()
** = Potencia
// = Divisão Inteira
% = Resto da Divisão 
*, /, 
+, -,

p = float(input('Digite o valor do produto R$ '))
descontcorrigido = float(input('Digite o valor do desconto '))
des = descontcorrigido / 100

Corecao = p - (p * des)

print('O porduto que custava R$ {:.2f}, na promoção com {:.0f} % de desconto, custa agora R$ {:.2f}' . format(p, des*100, Corecao))


x = 0  # Variável para contagem
valor_lido = 0  # Variável para armazenar o valor lido

while x < 10:  # Condição para parar o loop quando x for 10
  print(x)
  x += 1  # Incrementa x a cada iteraç
'''

import pyautogui as pg
from time import sleep

sleep(2)
# Define as coordenadas das posições
posicao_1 = (522, 308)  # Coordenadas x e y da primeira posição
posicao_2 = (531, 712)  # Coordenadas x e y da segunda posição
x = 0
# Função para clicar em uma posição
def clicar_posicao(posicao):
  """Clica na posição especificada por coordenadas (x, y)."""
  pg.click(x=posicao[0], y=posicao[1])  # Acessa x e y usando o índice

# Função para realizar ações de editar e salvar
def editar_e_salvar(texto_pesquisa):
  """Realiza as ações de pressionar F5, digitar texto, pressionar Enter e F6."""
  sleep(0.5)
  pg.press('F5')
  sleep(0.5)
  pg.write(texto_pesquisa)
  pg.press('enter')
  pg.press('F6')

# Loop para iterar por múltiplas seleções
for _ in range(4):  # O loop será executado 4 vezes
  clicar_posicao(posicao_1)
  sleep(1)  # Ajuste o tempo de espera (sleep) se necessário

  clicar_posicao(posicao_2)
  editar_e_salvar('2571')
  x += 1
  

