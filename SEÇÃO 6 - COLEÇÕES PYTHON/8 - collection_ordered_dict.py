from collections import OrderedDict
"""
dicionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
for chave, valor in dicionario.items():
    print(f"Chave={chave} : Valor={valor}")

dicionario["z"] = 26
for chave, valor in dicionario.items():
    print(f"Chave={chave} : Valor={valor}")

dicionario["m"] = 13
for chave, valor in dicionario.items():
    print(f"Chave={chave} : Valor={valor}")

dicionario = OrderedDict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
for chave, valor in dicionario.items():
    print(f"Chave={chave} : Valor={valor}")
"""
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}

print(dict1 == dict2)  # True. Ele não leva em conta a ordem

dict1 = OrderedDict({"a": 1, "b": 2})
dict2 = OrderedDict({"b": 2, "a": 1})

print(dict1 == dict2)  # False
