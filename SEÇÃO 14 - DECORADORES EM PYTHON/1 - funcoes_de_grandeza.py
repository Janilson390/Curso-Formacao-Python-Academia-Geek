"""
Funções de maior grandeza - Higher Order Functions (HOF)

- Quando uma linguagem suporta HOF, indica que podemos ter funções que retornam outras funções
como resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até
mesmo criar variáveis do tipo de funções nos nossos programas.


# Exemplo - Definindo as Funções

def soma(a, b):
    return a + b

def subtracao(a , b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return f"Erro na operação! {e}"

def calcular (num1, num2, funcao):
    return funcao(num1, num2)

print(calcular(5, 5, soma))
print(calcular(5, 5, subtracao))
print(calcular(5, 5, multiplicacao))
print(calcular(5, 5, divisao))
print(calcular(5, 0, divisao))


# Nested Functions - Funções Aninhadas

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(("E ai ", "Suma daqui ", "Gosto muito de você, "))
    return humor() + pessoa + "!"

print(cumprimento("Janilson"))
"""
# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(("hahahahahaha", "kakakakakakakakakaka", "rssssss..."))
    return rir
rindo = faz_me_rir()

print(rindo())