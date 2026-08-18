"""
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

media = statistics.mean(dados)

print(f"Media= {media}")

res = filter(lambda valor: valor < media, dados)
print(type(res))
lista_res = list(res)
print(list(res))
print(list(lista_res))

paises = ['', 'Aregentina', '', 'Estados Unidos', '', '', 'Brasil', 'Alemanha', 'Italia', '']
print(f"Paises= {paises}")

res = filter(None, paises)
print(type(res))
print(list(res))

res2 = filter(lambda pais: len(pais) > 0, paises)
print(type(res2))
print(list(res2))

res3 = [pais for pais in paises if len(pais) > 0]
print(type(res3))
print(list(res3))

# Exemplo complexo
usuarios = [
    {"username":"janilson", "tweets":["Eu gosto de churrassco"]},
    {"username":"jeff", "tweets":["Eu gosto de gato", "Não curto cachorro"]},
    {"username":"bob.6598", "tweets":[]},
    {"username":"janZek", "tweets":[]},
    {"username":"eu_a_lenda", "tweets":["Amo passear", "Vou a praia hoje. BORA!?"]}
]

print(usuarios)

# inativos = filter(lambda u: len(u["tweets"]) == 0, usuarios)
inativos = filter(lambda u: not len(u["tweets"]), usuarios)
print(list(inativos))
"""
nomes = ["Vanessa", "Ana", "Maria", "Sandra", "Marcela", "Lara", "Fábia", "Mayara"]

lista = list(map(lambda nome: f"Sua instrutora é {nome}", filter(lambda nome: len(nome) <= 5, nomes)))
print(lista)