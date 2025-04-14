

while 1 > 0:

    for i in range(11):

        if i == 0:
            num_tabuda = input('Digite um numero inteiro para ver sua tabuada: ')

            int_num_tab = int(num_tabuda)

        print('{} x {} = {}' .format(int_num_tab, i, int_num_tab * i))
        if i == 10:
            i = 0
