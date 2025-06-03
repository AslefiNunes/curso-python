import re
cpf_enviado_usuario = re.sub(r'[^0-9]', '', '71190628597')#Remove non-numeric characters
# Validar CPF : Precisa validar se os numeros não são todos iguais, calcular os dois dígitos verificadores e comparar com o CPF enviado pelo usuário.
'''
 cpf_invalido = '77777777777'
 verificar_se_repetidos = cpf_invalido == cpf_enviado_usuario[0] * 11 # Retorna Boolean
'''

nove_digitos = cpf_enviado_usuario[0:9]
cont_regressivo = 10
valor = 0

for i in nove_digitos:
    valor += int(i) * cont_regressivo
    cont_regressivo -= 1

resto = (valor * 10) % 11
resultado = 0 if resto > 9 else resto

cont_regressivo_2 = 11
valor_2 = 0
dez_digitos = nove_digitos + str(resultado)
for i in dez_digitos:
    valor_2 += int(i) * cont_regressivo_2
    cont_regressivo_2 -= 1
resto_2 = (valor_2 * 10) % 11
resultado_2 = 0 if resto_2 > 9 else resto_2
cpf_validado = dez_digitos + str(resultado_2)

if cpf_enviado_usuario == cpf_validado:
    print(f'O CPF {cpf_validado} VÁLIDO')
else:
    print('CPF INVÁLIDO')
