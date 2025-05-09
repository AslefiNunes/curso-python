'''
quant = int(input('Digite a quantidade de pessoas que você gostaria de cadastra: '))
imc = []
dados = []

if quant > 0:
    while True:
        nome = str(input('Digite nome: '))
        peso = int(input('Digite o peso: '))
        dados.append(nome)
        dados.append(peso)
        imc.append(dados[:])
        dados.clear()
        quant -=1
        if quant == 0:
            perg = str(input('Gostaria de continuar [S/N]')).upper().strip()[0]
            if perg == 'N':
                break
            else:
                quant = int(input('Digite a quantidade de pessoas que você gostaria de cadastra: '))

   
    contN = 0
    maiorP = 0
    menorP = 0

    for i in imc:
        if quant == 0:
            maiorP = i[1]
            menorP = i[1]
            quant += 1
        if i[0]:
            contN += 1
        if i[1] > maiorP:
            maiorP = i[1]
        else:
            if menorP > i[1]:
                menorP = i[1]
print(imc)
print(f'Foram cadastrada {contN}')
print(f'O maior peso é {maiorP} e o menor é {menorP}')'''


#RESPOSTA DO GUSTAVO:

temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input('Digite o nome da pessoa: ')))
    temp.append(int(input('Digite o peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    cont = str(input('Deseja continuar ?: '))
    if cont in 'Nn':
        break

print(f'Os dados foram {princ}')
print(f'O total de alunos cadastrados foi de {len(princ)} pessoas.')
print(f'O maior pessos foi {maior} KG peso de', end = '')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end = '')
print()
print(f'O menor pesso foi de {menor} KG. Peso de', end = '')
for p in princ:
    if p[1] == menor: 
        print(f'[{p[0]}]', end='')