print("Valor paradão é 0. O Valor final não é inclusive")
# No caso, ele vai de 0 a 9.
for i in range(10):
    print(i)

print("Valor inicial e valor de parada expecificos")
for i in range(1, 10):
    print(i)

for i in range(3, 10):
    print(i)


print("Valor inicial, valor de parada e passo expecificos")
for i in range(1, 10, 2):
    print(i)

for i in range(10, 30, 5):
    print(i)

print("Forma inversa: valor inicio, valor de parada e passo expecificos")
for i in range(10, 0, -1):
    print(i)

# Vai até o 0
for i in range(10, -1, -1):
    print(i)

# Convertendo um range em uma lista
lista = list(range(10))
print(lista)
