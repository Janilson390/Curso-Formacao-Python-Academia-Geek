from random import random

def quadrado_de_7():
    return 7 * 7

def diz_oi():
    return "oi"
    print("Executado depois do return!")

def diz_oi2():
    print("Executado antes do return!")
    return "oi"
    print("Executado depois do return!")

def nova_funcao():
    variavel = None
    if variavel:
        return "Verdadeiro"
    elif variavel is False:
        return "Falso"
    else:
        return "None"

def empacotador():
    return 2, 2, 3

def joga_moeda():
    valor = random()
    if valor > 0.5:
        return "Cara"
    return "Coroa"

# print(quadrado_de_7())


# print(diz_oi())
# print(diz_oi2())
# print(nova_funcao())
# n1, n2, n3 = empacotador()
# print(n1, n2, n3)
print(joga_moeda())
