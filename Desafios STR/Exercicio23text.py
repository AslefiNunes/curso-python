frase = " Curso em Video Python "

print(frase[3:13])

print(frase[:12])

print(frase[1:15:2])

print(frase.count('o'))

print(frase.upper().count("O"))

print(len(frase))

print(len(frase.strip()))

print(frase.replace('Python', 'Android'))

print('Curso' in frase)

print(frase.find('Python'))

print(frase[16])

print(frase.find('video')) # Observe que "video" esta em minusculo

print(frase.lower().find('video')) # Aqui ele transforma em minusculo 

print(frase.split())

dividido = frase.split()

print(dividido[0])