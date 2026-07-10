"""
Mapas = Dicionários
"""
receita = {"jan": 100, "fev": 200, "mar": 300}

# Iterar sobre dicionários
for chave in receita:
    print(chave, end=" ")

for chave in receita:
    print(receita[chave], end=" ")

for chave in receita:
    print(f"Em {chave} recebi R$ {receita[chave]}")

# Somente as chaves
print(receita.keys())

# Somente os valores
print(receita.values())

for chave in receita.keys():
    print(f"Em {chave} recebi R$ {receita[chave]}")

for valor in receita.values():
    print(f"Em R$ {valor}")

print(receita.items())
for chave, valor in receita.items():
    print(f"Em {chave} recebi R$ {valor}")

print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita.values()))
