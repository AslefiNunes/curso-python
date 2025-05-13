print('=' * 50)
print('{:-^40}' .format('Banco do Agro'))
print('=' * 50)
saque = int(input('Qual o valor do saque: R$ '))
ced = 50
totced = 0

while True:
    if saque >= ced:
        saque -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if saque == 0:
            break
print('=' * 50)
print('Volte sempre ao BANCO !')
''' Resposta Aslefi

print('=' * 20)
print('BACON DOS LISO')
print('=' * 20)
saque = int(input('Qual o valor do saque: R$ '))
ced = [1, 10, 20, 50]
n = 3
conta50 = conta20 = conta10 = conta1 = 0

while True:
    
    if saque >= ced[n]:
        if n == 3:
            conta50 += 1
        elif n == 2:
            conta20 += 1
        elif n == 1: 
            conta10 += 1
        elif n == 0:
            conta1 += 1
        
        saque = saque - ced[n]
        if saque < ced[n] and saque != 0:
            n -= 1
        else:
            if saque == 0:
                break
    else:
        if n >= 0:
            n -= 1
        else:
            break


print(f'{conta50} notas de R$ 50,00')
print(f'{conta20} notas de R$ 20,00')
print(f'{conta10} notas de R$ 10,00')
print(f'{conta1} notas de R$ 1,00')
print('=' * 20)
print('Volte sempre ao BANCO ! Tenha um bom dia!')'''

    
