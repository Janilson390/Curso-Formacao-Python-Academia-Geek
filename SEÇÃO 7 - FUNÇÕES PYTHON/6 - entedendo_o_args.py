def soma_valores(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma


def soma_valores2(*args):
    return sum(args)


def soma_valores3(nome, sobrenome, *args):
    return sum(args)


def verifica_info(*args):
    if "Geek" in args and "University" in args:
        return "Bem-vindo Geek!"
    return "Eu não te conheço!"


def soma_tudo(*args):
    return sum(args)


print(soma_valores())
print(soma_valores(1))
print(soma_valores(1, 2))
print(soma_valores(1, 2, 3))

print(soma_valores2())
print(soma_valores2(1))
print(soma_valores2(1, 2))
print(soma_valores2(1, 2, 3))

print(verifica_info())
print(verifica_info(1, True, "University", "Geek"))
print(verifica_info(1, "University", 3.145))

numeros = [1, 2, 3, 4, 5, 6, 70]
# print(soma_tudo(numeros))
# desempacotar
print(soma_tudo(*numeros))
