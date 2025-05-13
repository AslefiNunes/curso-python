# Leia o primeiro termo e a razão de uma  razão aritimetica.no final mostre os 10 primeiro termos - é uma sequência de números onde a diferença entre dois termos consecutivos é sempre a mesma. a sequência (4, 7, 10, 13, 16, ...) é uma P.A. infinita. a sequência (70, 60, 50, 40, 30, 20, 10) é uma P.A. finita.

pri_Termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = pri_Termo + (10 - 1) * razao

for i in range(pri_Termo, decimo + razao, razao):
    print(i, end=' ')