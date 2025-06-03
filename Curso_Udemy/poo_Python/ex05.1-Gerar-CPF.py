from random import randint

def gerar_digitos_cpf():
    nove_digitos = ''
    for criar_digito in range(9):
        nove_digitos += str(randint(0, 9))
    return nove_digitos

def calcular_digito(nove_digitos, cont_regressivo):
    valor = 0
    for i in nove_digitos:
        valor += int(i) * cont_regressivo
        cont_regressivo -= 1
    resto = (valor * 10) % 11
    return 0 if resto > 9 else resto

def gerar_cpf():
    nove_digitos = gerar_digitos_cpf()
    decimo_digito = calcular_digito(nove_digitos, 10)
    dez_digitos = nove_digitos + str(decimo_digito)
    decimo_primeiro_digito = calcular_digito(dez_digitos, 11)
    cpf_validado = dez_digitos + str(decimo_primeiro_digito)
    return cpf_validado

def main():
    cpf_gerado = gerar_cpf()
    print(f'O CPF gerado é: {cpf_gerado}')

for _ in range(5):
    main()