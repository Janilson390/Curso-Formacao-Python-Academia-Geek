# All() -> Retorna True se todo os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
"""
print(all([0, 1, 2, 3, 4, 5])) # False
print(all([1, 2, 3, 4, 5])) # True
print(all([])) # True
print(all((1, 2, 3, 4, 5))) # True
print(all({1, 2, 3, 4, 5})) # True
print(all('Geek')) # True
print(all(['Geek', ''])) # False

nomes = ['Cassio', 'Carlos', 'Carol', "Cleber"]

print(all([nome[0] == 'C' for nome in nomes])) # True

nomes.append('Fábio')

print(all([nome[0] == 'C' for nome in nomes])) # False

print(all([letra for letra in 'eiof' if letra in 'zxcv']))
"""

# Any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False.

print(any([0, 1, 2, 3, 4, 5])) # True
print(any([])) # False
print(any([0, False, {}, [], ()]))

nomes = ['Cassio', 'Carlos', 'Carol', "Cleber"]

print(any([nome[0] == 'C' for nome in nomes])) # True

nomes.append('Fábio')

print(any([nome[0] == 'C' for nome in nomes])) # True

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
