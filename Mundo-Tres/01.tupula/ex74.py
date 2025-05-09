from random import randint

n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print (n)  

print(max(n))
print(min(n))

'''from random import randint

n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)

tab = (n1,n2,n3,n4,n5)

print(tab)
print(max(tab))
print(min(tab))'''

'''from random import randint

n = [0] * 5

for c in range(0, 5):
    sort = randint(0, 10)
    n[c] = sort

nova_tupu = tuple(n)
print(nova_tupu)
print(f'O maior valor sorteado foi {max(nova_tupu)}')
print(f'O menor valor sorteado foi {min(nova_tupu)}')
'''