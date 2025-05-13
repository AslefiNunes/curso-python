from datetime import date


#Categorias
mirim = 9
infantil = 14
juvenil = 19
senior = 20
ano_atual = date.today().year
nasc = int(input('Qual o ano de nascimento do atleta? '))
idade = ano_atual - nasc

if idade <= mirim:
    print('O atleta tem {} anos e pertence a categoria MIRIM'.format(idade))
elif idade <= infantil: 
    print('O atleta tem {} anos e pertence a categoria INFANTIL'.format(idade))
elif idade <= juvenil:
    print('O atleta tem {} anos e pertence a categoria JUVENIL'.format(idade))
elif idade <= senior:
    print('O atleta tem {} anos e pertence a categoria SENIOR'.format(idade))
else:
    print('O atleta tem {} anos e pertence a categoria MASTER'.format(idade))
# Exemplo de execução:

