"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos.
2. Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa
deve executar os seguintes passos:
a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7.
b) Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre
na tela esta soma.
c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100.
d) Mostre na tela cada valor da lista A, um em cada linha.
3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.

print("1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos.
")

lista = []
cont = 1
while cont <= 6:
    lista.append(input(f"Digite o {cont}º valor: "))
    cont += 1

print(f"Os elementos dessa lista são {lista}\n")

print("2. Faça um programa que possua uma lista denominada A que armazene 6 números inteiros. O programa deve executar os seguintes passos: a) Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7. b) Armazene em uma variável inteira a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre na tela esta soma. c) Modifique a lista na posição 5, atribuindo a esta posição o valor 100. d) Mostre na tela cada valor da lista A, um em cada linha.") 

A = [1, 0, 5, -2, -5, 7]

soma = A[0] + A[1] + A[5]

A[5] = 100
print(f"Soma= {soma}")
for items in A:
    print(items)
"""
print("3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele possui.")

lista: list[int] = []
lista_pares: list[int] = []
cont: int = 1
pares: int = 0

while len(lista) < 10:
    valor: int = int(input(f"Digite o {cont} valor: "))
    lista.append(valor)

    if valor % 2 == 0:
        pares += 1
        lista_pares.append(valor)

    cont += 1

print(f"Existem {pares} números pares nessa lista e são eles: {lista_pares}.")
