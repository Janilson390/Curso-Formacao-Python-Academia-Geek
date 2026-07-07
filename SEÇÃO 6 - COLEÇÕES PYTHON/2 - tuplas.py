"""
print(type(()))

# Tuplas são representadas por parênteses, mas veja:
tupla1 = (1, 2, 3, 4)  # Isso é uma tupla
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4  # Isso é uma tupla
print(tupla2)
print(type(tupla2))

# Tuplas com um elemento
tupla3 = (1)  # Isso NÃO é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (1,)  # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 1,  # Isso é uma tupla
print(tupla5)
print(type(tupla5))
# Ná definição, o que define uma tupla é a virgula ,

# Podemos gerar uma tupla com range
tupla6 = tuple(range(11))
print(tupla6)
print(type(tupla6))

tupla7 = ("Geek University", "Programação em Python")
escola, curso = tupla7
print(tupla7)
print(escola)
print(curso)
print(type(tupla7))

# Métodos de adição e remoção de elementos não existem, pelo fato de seram imutáveis
# Mas os métodos SUM*, Min, Max e Len continuam funcionando
# * Para valore sinteiros e reias

tupla8 = (1, 2, 3, 4, 5, 9, 0)
print(tupla8)
print(sum(tupla8))
print(min(tupla8))
print(max(tupla8))
print(len(tupla8))

# Concatenação de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2

print(tupla1)
print(tupla2)
print(tupla3)

tupla1 = tupla3
print(tupla1)

#Encontar elemento em um tupla
tupla1 = (1, 0, 2, 3, 6, 8, 9)
print(8 in tupla1)
print(3 in tupla1)
print(10 in tupla1)

# Iteração em uma tupla
tupla = ("a", "b", "c", "d", "e", "f")
print(tupla)

for elemento in tupla:
    print(elemento)

for indice, elemento in enumerate(tupla):
    print(indice, elemento)

    # Contando elementos dentro de uma tupla
tupla = ("f", "a", "b", "c", "d", "e", "f")
print(tupla.count("a"))
print(tupla.count("f"))

escola = tuple("Geek University")
print(escola)
print(escola.count("e"))

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
print(meses)
print(meses.index("Agosto"))
print(len(meses))
"""
# Copiando uma tupla
tupla = (1, 2, 3)
print(tupla)

nova = tupla
print(nova)

outra = nova + tupla

print(outra)
print(dir(tupla))
