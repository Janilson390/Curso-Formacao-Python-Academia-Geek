from collections import defaultdict
"""
# Recap dicionário
dicionario = {"curso": "Programação em Python"}

print(dicionario)
print(dicionario["curso"])
print(dicionario["outro"])  # KeyError
"""
# Eu defino quelauer valor como default
# dicionario = defaultdict(lambda: 0)
dicionario = defaultdict(lambda: "None")

dicionario["curso"] = "Programação em Python"

print(dicionario)
print(dicionario["curso"])
print(dicionario["outro"])
