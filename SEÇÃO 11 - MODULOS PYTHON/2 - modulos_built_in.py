"""
'from random import *' É diferente de 'import random' -> Colocando o *, precisamos só chamar a função. na segunda forma, teremos que chamar
a biblioteca também, como por exemplo random.random().

from random import *
print(random())
print(randint(1, 10))

# Alias no modulo
import random as rdm
print(rdm.random())
print(rdm.randint(1, 10))


# Alias na função
from random import random as rdm, randint as rdt

print(rdm())
print(rdt(1, 10))

"""
# Pode colocar vários imports em uma TUPLA
from random import (random, randint,
                    shuffle, choice)

print(random())
print(randint(2, 60))

lista = ["Geek", "University", "Python"]
shuffle(lista)
print(lista)

print(choice("University"))

