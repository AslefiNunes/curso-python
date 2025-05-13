a, b = 0, 1

for i in range(15):
    print(a, end=' ')
    a ,b = b, a + b

# Segundo metodo

C, T1, T2 = 3, 0 , 1

def fibonacci(A, B):
     f = A + B
     print(f, end=' ')
     A = B
     B = f
     return A, B

print(T1, end=' ')
print(T2, end=' ')

for i in range(C, 16):
   T1, T2 = fibonacci(T1, T2)

