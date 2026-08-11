# Funções
def quadrado1(numero=0):
    return numero * numero


def quadrado2(numero):
    return numero ** 2


def parabens(nome):
    print("Parabéns pra você!")
    print("Nessa data querida!")
    print("Muitas felicidades!")
    print("Muitos anos de vida!")
    print(f"VIVA {nome}!")


def multiplicação(p1, p2, p3):
    return (p1 + p2) * p3


def nome_completo(nome, sobrenome):
    return f"{nome} {sobrenome}"


# print(f"Resultado={quadrado2()}") # TypeError
# print(f"Resultado={quadrado1(2)}")  # TypeError
# print(f"Resultado={quadrado1(9)}")
# print(f"Resultado={quadrado2(9)}")

# parabens("Janilson")
# print(multiplicação(2, 5, 6))
# print(multiplicação(2, 5, " NaN ") + " BATMAN!")

n = "Janilson"
s = "Florencio"
print(nome_completo(n, s))
print(nome_completo(s, n))
# Nomeando os parâmetros
print(f"Seu nome é {nome_completo(nome=n, sobrenome=s)}")
print(f"Seu nome é {nome_completo(nome="Janilson", sobrenome="Florencio")}")
print(f"Seu nome é {nome_completo(sobrenome=s, nome=n)}")
