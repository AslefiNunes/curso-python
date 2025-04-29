print('Gerador de PA')
print('=-=' * 10)

t1 = int(input('Primeiro termo: '))
ra = int(input('Razão da PA: '))
esco = int(input('Quantos termos voce que mostra: '))
cont = 0
total = 0


while True:
    if esco != 0:
        print(t1, end = " ")
        t1 += ra
        cont += 1
        total += 1
        if cont == esco:  
            esco = int(input('Pause \n Quantos termos você quer mostra: '))
            while esco * 0 != 0:
                esco = int(input('Digite um valor valido: '))
            if esco == 0:
                print(f'PA finalizada com {total} termos')
                break
            else:
                cont = 0
    else:
        print(" Você não quis mostra nem um termo! ")
        break