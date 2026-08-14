dicionario = {"a": 1, "b": 2, "c": 3}

res = {chave: valor * 2 for chave, valor in dicionario.items()}

print(res)

numeros = [1, 2, 3, 4]

quadrado = {valor: valor ** 2 for valor in numeros}

print(quadrado)

chaves = "abcde"
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

res = {num:("par" if not num % 2 else "impar") for num in numeros}
print(res)