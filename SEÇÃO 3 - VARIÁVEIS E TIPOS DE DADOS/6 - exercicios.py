# 1 - Faça um programa que leio um número inteiro e imprima-o

nummero = int(input("DIgite um numero inteiro: "))

print(f"O número digitado é o {nummero}!")

# 2 - Faça um programa que peça ao usuário digitar três valores inteiros e imprima a soma deles

soma = 0
i = 0
while i < 3:
    valor = int(input(f"Digite o {i+1}º valor: "))
    soma += valor
    i += 1

print(f"A soma deles é {soma}!")

# 3 - Faça um programa que receba três valores e apresente a soma dos quadrados dos valores lidos

soma = 0
i = 0
while i < 3:
    valor = int(input(f"Digite o {i+1}º valor: "))
    soma += valor**2
    i += 1

print(f"A soma dos quadrados é {soma}!")
