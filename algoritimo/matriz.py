miD = [[1,2,3], [1,2,3], [1,2,3]]


for i in range(3):
    for j in range(3):
        if i == j:
            miD[i][j] = 1
        else:
           miD[i][j] = 0

for linha in miD:
    print(linha)