pares = [numero for numero in [1, 2, 3, 4, 5, 6] if numero % 2 == 0]
impares = [numero for numero in [1, 2, 3, 4, 5, 6] if numero % 2 == 1]

print(pares, impares)

# Refatorando
print("Pares= ", [numero for numero in [1, 2, 3, 4, 5, 6] if not numero % 2])
print("Impares= ", [numero for numero in [1, 2, 3, 4, 5, 6] if numero % 2])

print([numero * 2 if numero % 2 == 0 else numero /2 for numero in [1, 2, 3, 4, 5, 6]])
