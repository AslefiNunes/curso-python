frase = str(input('Digite uma frase: ')).strip().upper()

count = frase.count('A')

print(f'A letra "A" aparece {count} vezes na frase.')
print('A primeira letra "A" aparece na posição {}'.format(frase.find('A')+1))
print('A última letra "A" aparece na posição {}'.format(frase.rfind('A')+1))

