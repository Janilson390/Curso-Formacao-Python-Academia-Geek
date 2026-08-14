num = {1, 2, 3, 4}

res = {num ** 2 for num in num}

print(res)

numeros = {num for num in range(1, 7)}
print(numeros)

numeros = {num: num ** 2 for num in range(1, 7)}
print(numeros)

letras = {letra for letra in "Geek University"}
print(letras)
