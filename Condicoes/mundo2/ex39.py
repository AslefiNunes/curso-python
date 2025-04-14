from datetime import date

ano = int(input("Digite o ano em que você nasceu: "))

ano_atual = date.today().year
idade = ano_atual - ano

if idade < 18:
    print(f"Você ainda não pode se alistar. Você tem {idade} anos.")
    print(f'Faltam {18 - idade} anos para você se alistar.')
elif idade == 18:
    print(f"Você deve se alistar. Você tem {idade} anos.")
else:
    print(f"Você já passou do prazo para se alistar. Você tem {idade} anos e já passou {(idade - 18)} anos.")
