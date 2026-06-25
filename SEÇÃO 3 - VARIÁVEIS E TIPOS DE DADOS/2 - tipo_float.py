"""
Tipo Float

Tipo real, decimal

Casas decimais
"""
# Errado
valor1 = 1, 44
print(valor1)
print(type(valor1))

# Certo
valor1 = 1.44
print(valor1)
print(type(valor1))

# Dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# COnversão de float para int
valor1 = 1.44
res = int(valor1)
print(res, type(res))

# Números complexos
complexo = 5j
print(complexo, type(complexo), complexo ** 2)

print(dir(valor1))
