
num1 = input('Primeira nota do Aluno: ')
num2 = input('Segunda nota do Aluno: ')

int_num1 = float(num1)
int_num2 = float(num2)

media = (int_num1 + int_num2) / 2

print('A media entre{:.2f} e {:.2f} é igual a {:.2f}' .format(int_num1, int_num2, media))