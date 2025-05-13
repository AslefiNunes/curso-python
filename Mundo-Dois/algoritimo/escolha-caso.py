"""
valor = int

print("------------------------------------------")
print("Bem-vindo ao programa de escolha de caso!")
print("------------------------------------------")
print("")
print("[1] - para a primeira opção")
print("[2] - para a segunda opção") 
print("[3] - para a terceira opção")
print("[4] - para a quarta opção")
print("[5] - para cancelar")
print("")
opcao = int(input("Digite a opção desejada: "))
match opcao:
    case 1:
        valor = 10
    case 2:
        valor = 20
    case 3:
        valor = 30
    case 4:
        valor = 50
    case 5:
        print("Operação cancelada.")
    case _:
        print("Opção inválida. Por favor, escolha uma opção válida.")

print("------------------------------------------")
print("Você ganhou: RS {} no pix" .format(valor))
print("------------------------------------------")


print("Fim do programa.")

"""

func = str(input("Digite o nome do funcionario: "))
salario = float(input("Digite o salario do funcionario: "))
dep = int(input("Digite o numero de dependentes: "))

match dep:
    case 0:
        salario = salario
    case 1, 2, 3, 4:
        salario = salario + (65 * dep)
    case _:
        salario = salario + (65 * dep)

print("O funcionario {} tem salario de R$ {:.2f} e {} dependentes." .format(func, salario, dep))
    