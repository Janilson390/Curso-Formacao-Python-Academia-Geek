instrutor = "Java"


def fun_global():
    return instrutor


def fun_local():
    instrutor = "Python"
    return instrutor


def fun_local2():
    global instrutor
    instrutor = "Python"
    return instrutor


def mostra_instrutor(nome="Geek", instrutor=False):
    if nome == "Geek" and instrutor:
        return "Bem-vindo instrutor Geek"
    elif nome == "Geek":
        return "Eu pensei que você era o instrutor!"
    return f"Olá {nome}"


def multiplicação(p1=1, p2=1, p3=0):
    return (p1 + p2) * p3


def nome_completo(nome="Fulano", sobrenome="de Tals"):
    return f"{nome} {sobrenome}"


def exponencial(numero=2, potencia=2):
    return numero ** potencia


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def matematica(num1, num2, fun=soma):
    return fun(num1, num2)


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()


"""
print(exponencial())
print(exponencial(5))
print(exponencial(5, 5))
print(exponencial(potencia=10, numero=1000))

print(nome_completo())
print(nome_completo("Janilson"))
print(nome_completo(sobrenome="da Silva"))

print(mostra_instrutor())
print(mostra_instrutor(instrutor=True))
print(mostra_instrutor(True))
print(mostra_instrutor("Ozzy"))
print(mostra_instrutor(nome="Janilson"))


# Passando função como parametro
print(matematica(5, 6))
print(matematica(5, 6, subtracao))
# print(matematica(soma)) TypeError

print(fun_global())
print(fun_local())
print(fun_local())
print(fun_global())
"""
print(fora())
# print(dentro()) NameError: name 'dentro' is not defined
