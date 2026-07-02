
print("\n1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, \nconsiderando números maiores que 0.")
print("Multiplos de 3:")

contador = 0
for i in range(100):
    if i > 0 and i % 3 == 0:
        print(f"O número {i} é multiplo de 3.")
        contador += 1

    if contador == 5:
        break


contador = 0
indice = 1

while contador < 5:
    if indice % 3 == 0:
        print(f"O número {indice} é multiplo de 3.")
        contador += 1
    indice += 1

print("\n2. Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, \niniciando em 10 e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.")
print("Contagem regressiva")
cont = 10
while cont >= 0:
    print(cont)
    cont -= 1
print("FIM")

print("3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, \nimprimindo seu valor na tela, até que seu valor seja 100000 (cem mil).")
numero = 0
while numero <= 100000:
    print(numero, end=", ")
    numero += 1000

print("\nCom FOR\n")
for n in range(0, 100001, 1000):
    print(n, end=", ")
