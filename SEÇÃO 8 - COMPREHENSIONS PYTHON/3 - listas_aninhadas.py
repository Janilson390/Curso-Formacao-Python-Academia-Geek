listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
for lista in listas:
    for num in lista:
        print(num)
"""
# Mesma coisa do exemplo acima
[[print(valor) for valor in lista] for lista in listas]

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

print(tabuleiro)

velha = [["X" if numero % 2 == 0 else "O" for numero in range(
    1, 4)] for valor in range(1, 4)]

for lista in velha:
    print(lista)

print([["*" for i in range(1, 4)] for j in range(1, 4)])
