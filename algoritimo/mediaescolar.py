n1 = float(input("Digite a nota do primeiro bimestre: "))
n2 = float(input("Digite a nota do segundo bimestre: "))

m = (n1 + n2) / 2

if m >= 9:
    print("A media do aluno é: {:.2f} e a clasificacao é A" .format(m))
elif m >= 8 and m <= 8.9:
    print("A media do aluno é: {:.2f} e a  clasificacao é B" .format(m))
elif m >= 7 and m <= 7.9:
    print("A media do aluno é: {:.2f} e a clasificacao é C" .format(m))
elif m >= 6 and m <= 6.9:
    print("A media do aluno é: {:.2f} e a clasificacao é D" .format(m))
elif m >= 5 and m <= 5.9:
    print("A media do aluno é: {:.2f} e a clasificacao é E" .format(m))
else:
    print("A media do aluno é: {:.2f} e a clasificacao é F" .format(m))

