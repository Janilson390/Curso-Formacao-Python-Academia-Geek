"""
List Comprehension: grar uma lista processada apartir de outra lista
# Sintaxe
[dado for dado in interavél]
"""


def funcao(valor):
    return valor * valor


def caixa_alta(nome: str):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

# numeros = [1, 2, 3, 4, 5]

# res = [numero * numero for numero in numeros]
# res = [funcao(numero) for numero in numeros]

# print(res)


# Loop vs Comprehension
numeros = [1, 2, 3, 4, 5, 6]
# numeros_dobrados = []

# for numero in numeros:
#    numero_dobrado = numero * 2
#    numeros_dobrados.append(numero_dobrado)

# print(numeros_dobrados)

# numeros_dobrados = []
# numeros_dobrados = [numero * 2 for numero in numeros]
print([numero * 2 for numero in numeros])

nome = "Geek University"
print([letra.upper() for letra in nome])

amigos = ["maria", "joão", "josé", "pedro"]

print([amigo.upper() for amigo in amigos])

print([caixa_alta(amigo) for amigo in amigos])

print([numero * 9 for numero in range(1, 11)])

print(bool(valor) for valor in [0, [], "", 1, True, 3.145])

print([str(valor) for valor in [1, 2, 3, 4, 5]])
