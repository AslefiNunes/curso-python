#Variaveis locais
def local(a, b):
    a = a + 1
    b = b + 1
    print(a, b)
    

x , y = 1, 1
local(x, y)
print(x, y)


# Atualizando Variaveis globais

print(" ")

def global_var(c, d):
    print(c, d)
    c = c - 1
    d = d - 1    
    return c, d
z, w = 1, 1
z, w = global_var(z, w)
print(z, w)