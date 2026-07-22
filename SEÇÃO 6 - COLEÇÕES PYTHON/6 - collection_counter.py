# Importando o Countrer
from collections import Counter
"""
lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 1, 2, 1, 3, 3, 1, 1, 2, 2, 4, 4, 5]

# Utilizando o counter
res = Counter(lista)
print(type(res))
print(res)

# Counter({1: 9, 2: 5, 3: 5, 4: 2, 5: 1})
# Para cada elemento da lista ele criou uma chave e colocou o valor da chave a quantidade de ocorrências.

print(Counter("Geek University"))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""
texto = """A língua cavineña, também conhecida como kavinenya, caviña ou kabineña, é um idioma pertencente à família takana do tronco linguístico pano-takana. É utilizada pelo povo cavineño, o qual tem sua comunidade majoritariamente localizada nos departamentos de Beni e Pando, no norte da Bolívia. Em resumo, é uma língua muito interessante e chata."""

palavras = texto.split()
# print(palavras)
res = Counter(palavras)

print(res)
# As 5 palavras com mais ocorrências
print(res.most_common(5))
