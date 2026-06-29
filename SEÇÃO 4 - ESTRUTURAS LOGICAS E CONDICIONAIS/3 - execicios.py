print("1 - Faça um programa que receba dois números inteiros e mostre qual deles é o maior.\n".title())
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}!")
elif num2 > num1:
    print(f"{num2} é maior que {num1}!")
else:
    print("Os números são iguais!")

print("2 - Faça um programa que leia um número inteiro fornecido pelo usuário.\
      Se esse número for positivo, calcule a raiz quadrada do número e apresente-a.\
      Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.\n".title())

num3 = input("Digite um numero: ")
raiz = float(num3) ** 0.5

if raiz > 0:
    print(f"A raiz de {num3} é {raiz}!")
else:
    print(f"Número inválido!")

print("3 - Fala um programa que recebe um número inteiro e informe se este número é par ou impar.\n".title())
num4 = input("Digite um numero: ")

if int(num4) % 2 == 0:
    print(f"{num4} é par!")
else:
    print(f"{num4} é impar!")
