num = int(input("Digite um numero entre 0 e 9999: "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"A unidade é {u}")
print("A dezena é {}" .format(d))
print(f"A centena é {c}")
print(f"A milhar é {m}")