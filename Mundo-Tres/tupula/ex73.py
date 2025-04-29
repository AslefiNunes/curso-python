times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Red Bull Bragantino', 'Ceara', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Juventude', 'Sao Paulo', 'Mirassol', 'Internacional', 'Bahia', 'Fortaleza', 'Botafogo', 'Vitória', 'Atletico Mineiro', 'Santos', 'Gremio', 'Sport Club do Recife')

select = str(input('Qual time você gostaria de saber a posição: '))
n = times.index(select) + 1
if select not in times:
    print('O time foi Rebaixado')
else:
    print(f'O {select} esta na posição {n}º')

print(times[:5])
print(times[-5:])
print(sorted(times))

