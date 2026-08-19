"""
Generators

Tuple Comprehension são na verdade Generators

nomes = ['Cassio', 'Carlos', 'Carol', "Cleber", "Fábio"]

print(any([nome[0] == "C" for nome in nomes]))

# List Comprehension
res = [nome[0] == "C" for nome in nomes]
print(type(res))
print(res)

# Generators
res = (nome[0] == "C" for nome in nomes)
print(type(res))
print(res)
print(tuple(res))
"""
from sys import getsizeof # retorna a quantidade de bytes em mémoria 

"""
print(getsizeof(" "))
print(getsizeof("Geek"))
print(getsizeof("University"))
print(getsizeof("1"))
print(getsizeof(1))
print(getsizeof(9))
print(getsizeof(95674464131844849))
print(getsizeof(True))
print(getsizeof(False))
"""

lista_comp = getsizeof([num * 10 for num in range(10000)])
set_comp = getsizeof({num * 10 for num in range(10000)})
dic_comp = getsizeof({num:num * 10 for num in range(10000)})
gen = getsizeof((num * 10 for num in range(10000)))

print(lista_comp)
print(set_comp)
print(dic_comp)
print(gen)

gen = (num * 10 for num in range(10000))
print(type(gen))
print(gen)
for num in gen:
    print(num)