"""
**kwargs
Exige que utilizemos parâmetros nomeados, e transforma esses parâmetros 
extras em um diccionário.
"""
# Exemplo


def cores_favoritas(**kwargs):
    # print(kwargs)
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita de {pessoa.capitalize()} é {cor}")


def cumprimento_especial(**kwargs):
    if "geek" in kwargs and kwargs["geek"] == "Python":
        return "Você recebeu um cumprimento Pythônico Geek!"
    elif "geek" in kwargs:
        return f"{kwargs['geek']} Geek!"
    return "Não tenho certeza quem você é ..."


"""
Nas funções, podemos ter NESSA ordem:
- Parâmetros obrigatórios;
- *args;
- Parâmetros default;
- **kwargs
"""


def minha_funcao(idade, nome, *args, soltero=False, **kwargs):
    print(f"{nome} tem {idade} anos!")
    print(args)
    if soltero:
        print("Solteiro")
    else:
        print("Casado")
    print(kwargs)


def mostra_nome(**kwargs):
    return f"{kwargs["nome"]} {kwargs["sobrenome"]}!"


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)


# cores_favoritas(marcos="verde", julia="amarelo", fernanda="azul", vanessa="branco")

# cores_favoritas()
# cores_favoritas(geek="navy")

# print(cumprimento_especial())
# print(cumprimento_especial(geek="Python"))
# print(cumprimento_especial(geek="Oi"))
# print(cumprimento_especial(geek="especial"))

# minha_funcao(8, "Julia")
# minha_funcao(18, "Felicity", 4, 5, 3, soltero=True)
# minha_funcao(34, "Felipe", eu="Não", voce="Vai")
# minha_funcao(19, "Carla", 9, 4, 3, java=False, python=True)


# Desenpacotar
# nomes = {"nome": "Janilson", "sobrenome": "Florencio"}
# print(mostra_nome(nomes)) TypeError
# print(mostra_nome(**nomes))

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)
# OBS: os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função
# dicionario = dict(d=1, e=2, f=3) TypeError
soma_multiplos_numeros(**dicionario)

# dicionario = dict(a=1, b=2, c=3, lang="Geek")

soma_multiplos_numeros(**dicionario, lang="Python")
