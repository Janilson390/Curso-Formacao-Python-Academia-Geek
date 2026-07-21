"""
# Definando um conjunto (Set)
# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Tem valores repetidos
print(s)
print(type(s))
# Caso um valor já existente seja adicionado no consulto, o mesmo será ignorado.

# Forma 2
s = {1, 2, 3, 4, 5, 5}  # Tem valores repetidos
print(s)
print(type(s))

# Convertendo Tipos
s = set("Geek University")
print(s)

lista = [1, 2, 3, 6, 3, 2, 1]
s = set(lista)
print(s)

tupla = (1, 2, 3, 6, 3, 2, 1)
s = set(lista)
print(s)

print(dir(s))

# Verificando se um elemento está no conjunto
if 3 in s:
    print("Tem o 3")
else:
    print("Não tem o 3")

# Importante lembrar que, além de não termos valores duplicados, não termos ordem
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f"Lista: {lista} com {len(lista)} elementos!")

tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f"Tupla: {tupla} com {len(tupla)} elementos!")

docionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], "dict")
print(f"Dicionário: {docionario} com {len(docionario)} elementos!")

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f"Conjunto: {conjunto} com {len(conjunto)} elementos!")

s = {1, "mamão", True, 56.3, False}
print(s)
print(type(s))

for valor in s:
    print(valor)

# Adicionando elemntos em um conjunto
s = {1, 2, 3}
print(s)

s.add(4)
print(s)

# Remover elementos
# Forma 1
s.remove(3)
print(s)

# Forma 1
s.discard(2)
print(s)

# Limpar uma lista
s = {1, 2, 3}
print(s)

s.clear()
print(s)

conjunto1 = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
conjunto2 = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}

# União
# Forma 1
uniao1 = conjunto1.union(conjunto2)
print(uniao1)

# Forma 2
uniao2 = conjunto1 | conjunto2
print(uniao2)

# Interção
# Forma 1
inter1 = conjunto1.intersection(conjunto2)
print(inter1)

# Forma 2
inter2 = conjunto1 & conjunto2
print(inter2)

# Diferença
# Forma 1
diff1 = conjunto1.difference(conjunto2)
print(inter1)

diff2 = conjunto2.difference(conjunto1)
print(diff2)
"""
s = {1, 2, 3, 4, 5}
print(f"Soma= {sum(s)}")
print(f"Máximo= {max(s)}")
print(f"Mínimo= {min(s)}")
print(f"Tamanho= {len(s)}")
