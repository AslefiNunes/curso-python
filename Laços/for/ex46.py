# faça contagem regressiva de 10 a 0 durando 1 segundo para estourar os fogos de artificio. emoji dos fogos de artificio!

from time import sleep

for i in range(10, 0, -1):
    sleep(1)
    print(i)

sleep(1)
print(' 🎆🎇')