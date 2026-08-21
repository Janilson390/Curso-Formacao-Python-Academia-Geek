"""
# sort() -> Só funciona só com lista
lista = [4, 5, 8, 2, 0, 9]

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

# sorted() -> Funciona com qualquer iterável

numeros = {4, 5, 8, 2, 0, 9}
print(numeros)

print(sorted(numeros)) # Ordenou em ordem crescente. Sempre retorna uma LISTA
print(numeros)

lista = [4, 5, 8, 2, 0, 9]
print(sorted(lista))
print(lista)

print(sorted(numeros, reverse=True)) # Ordenou em ordem decrescente

usuarios = [
    {"username":"janilson", "tweets":["Eu gosto de churrassco"]},
    {"username":"jeff", "tweets":["Eu gosto de gato", "Não curto cachorro"]},
    {"username":"bob.6598", "tweets":[], "cor": "Amarelo"},
    {"username":"janZek", "tweets":[]},
    {"username":"eu_a_lenda", "tweets":["Amo passear", "Vou a praia hoje. BORA!?"], "cor":"Preto", "musica":"rock"}
]

# Dá TypeError. Para dicionários, precisa colocar outro parametro
# print(sorted(usuarios))

print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
"""

musicas = [
    {"titulo":"Jerusalém", "tocou":5},
    {"titulo":"Tem sabor de mel", "tocou":1},
    {"titulo":"Meus próprios meios", "tocou":3},
    {"titulo":"Eu navegarei", "tocou":9},
    {"titulo":"Eis que estou a porta e bato", "tocou":2}
]

print(f"As musicas mais tocadas -> {sorted(musicas, key=lambda musica: musica["tocou"], reverse=True)}\n")

print(f"As musicas menos tocadas -> {sorted(musicas, key=lambda musica: musica["tocou"])}")