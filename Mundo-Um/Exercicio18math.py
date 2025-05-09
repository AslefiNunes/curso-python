import math
an = float(input('digite o angulo: '))
sen = math.sin(math.radians(an))
con = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O angulo de {} tem o SENO de {:.2f}, o COSENO é {:.2f}, e a TANGENTE é {:.2f}' .format(an, sen, con, tan))