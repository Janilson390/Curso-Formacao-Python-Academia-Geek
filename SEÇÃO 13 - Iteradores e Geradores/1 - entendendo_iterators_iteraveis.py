"""
Iterator: um objeto que pode ser iterado. Retorna um dado, sendo um elemento por vez quando uma funçao next() é chamada.
Iterable: Um objeto que irá retornar um iterator quendo a função iter() for chamada.
"""

nome = "Geek"
numeros = [1, 2, 3, 4, 5]

# print(next(nome))

itl1 = iter(nome)
itl2 = iter(numeros)

print(next(itl1))
print(next(itl1))
print(next(itl1))
print(next(itl1))

print(next(itl2))
print(next(itl2))
print(next(itl2))
print(next(itl2))
print(next(itl2))

for letra in nome:
    print(letra)
