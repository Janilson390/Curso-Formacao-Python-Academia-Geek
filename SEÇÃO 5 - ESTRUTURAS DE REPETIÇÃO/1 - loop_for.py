"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Tem que transforma-lo em uma lista

for letra in nome:
    if letra != " ":
        print(f"Me dê um {letra.upper()}")

for item in lista:
    print(f"Item {item}")

for numero in range(1, 10):
    print(numero)

for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

# QUando não precisamos de um valor, podemos descartá-lo utilizando um undeline (_)
for _, letra in enumerate(nome):
    print(letra)

    
qtd = int(input("Quantas vezes esse loop vai e impresso? "))

print("Loop repetindo ...")
for n in range(1, qtd+1):
    if n == 1:
        print(f"{n} Vez ...")
    else:
        print(f"{n} Vezes ...")

qtd = int(input("Quantas vezes esse loop vai e impresso? "))
soma = 0

for n in range(1, qtd+1):
    if n == 1:
        print(f"{n} Vez ...")
    else:
        print(f"{n} Vezes ...")

    soma += n
print(f"A soma é {soma}")
"""

# Imprimir o nome na mesma linha
nome = "Geek University"
for letra in nome:
    print(letra, end="")

print("\n")

# Original: U+1F60D
# Modificado: U0001F60D
for _ in range(3):
    for num in range(1, 11):
        print("\U0001F60D" * num)
