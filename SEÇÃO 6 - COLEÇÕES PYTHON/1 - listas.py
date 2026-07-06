"""
# Lista vazia
print(type([]))

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n',
          'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
# Atribuindo uma lista vazia a variável
lista3 = []
lista4 = list(range(11))
# Transformando a String em uma lista
lista5 = list("Geek University")

print(lista1)
print(lista2)
print(lista3)
print(lista4)

# Chegando um valor existente na lista
num = 8  # int(input("Digite um valor: "))
if num in lista4:
    print(f"Encontrei o número {num}!")
else:
    print(f"Não eEncontrei o número {num}!")

letra = "y"
if letra in lista2:
    print(f"Encontrei a letra {letra}!")
else:
    print(f"Não encontrei a letra {letra}!")

# Podemos ordenar uma lista
lista1.sort()
print(lista1)

lista2.sort()
print(lista2)

# Ordenar sem precisar ordenar primeiro para depois imprimir
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n',
          'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(sorted(lista1))
print(sorted(lista2))

# Contando as ocorrências
print("\nOcorrênccias")
print(lista1.count(1))
print(lista2.count("e"))

# Adicionando um novo item a lista
lista1.append(1000)
print(sorted(lista1))

# TypeError: list.append() takes exactly one argument (3 given)
# lista1.append(1001, 1002, 1003)
# print(sorted(lista1))

lista1.append([1001, 1002, 1003])  # Aceita só valor uúnico
print(lista1)

# Aceita várioos valores e adiciona individualmente
lista1.extend([1004, 1005, 1006])
print(lista1)

# Inserindo um elemento em uma lista em qualquer posição
lista6 = list(range(6))
print(lista6)
lista6.insert(3, "Novo valor")
print(lista6)

# Juntado listas
lista7 = list("GeekUniversity")
lista8 = list(range(11))
lista9 = lista7 + lista8
print(lista9)


lista10 = list("GeekUniversity")
lista10.extend(list(range(11)))

print(lista10)

# Forma 1 de reversão
lista10.reverse()
print(lista10)

# Forma 2 de reversão
lista11 = list("GeekUniversity") + list(range(11))
print(lista11[::-1])

# Tamanho de uma lista
print(len(lista11))

# Remover o ultimo elemanto de uma lista
print(lista11)
print(lista11.pop())
print(lista11)

# Removendo o elemento pelo indice
lista11.pop(2)
print(lista11)

# Limpando a lista
lista11.clear()
print(lista11)

# Repetir elemento em uma lista
lista11 = list(range(6))
print(lista11)
lista11 = lista11 * 3
print(lista11)

# Convertendo uma string em lista
lista11.clear()
curso = "Programação em Python: Essencial"
lista11 = curso.split()
print(curso)
print(lista11)
lista11.clear()
curso = "Programação,em,Python,Essencial"
lista11 = curso.split(",")
print(curso)
print(lista11)

# Convetendo uma lista em string
lista11.clear()
lista11 = ['Programação', 'em', 'Python', 'Essencial']
curso = " ".join(lista11)
print(curso)


carrinho = []
produto = ""

while produto != "sair":
    produto = input(
        "Adicione um produto na lista ou digite 'sair' para encerrar: ")
    if produto != "sair":
        carrinho.append(produto.upper())

print(f"Há {len(carrinho)} itens da lista:")
for item in carrinho:
    print(item)
"""

cores = ["verde", "amarelo", "azul", "branco"]

# Listanto com índices positivos
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3] + "\n\n")

# Listanto com índices negativos. Fica como se o lista fosse uma roda
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

for indice, cor in enumerate(cores):
    print(indice, cor)

numeros = [5, 6, 20, 79, 4, 220, 20]
print(numeros.index(20))
print(numeros.index(20, 3))

print(cores.index("branco"))

print(numeros[::])
print(numeros[2:3:2])
print(numeros[:4])
print(numeros[::2])

print(sum(numeros))
print(min(numeros))
print(max(numeros))
print(len(numeros))

num1, num2, num3, num4, num5, num6, num7 = numeros
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
print(num7)
