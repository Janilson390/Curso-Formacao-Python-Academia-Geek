x = 0

while x <= 10:
    print(f"Valor de x= {x}")

    if x == 6:
        break

    x += 1

numeros = [1, 3, 5, 7, 8, 9, 10]

print(numeros)
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} Numero par!")
        break
    else:
        print(f"{numero} Numero impar!")
