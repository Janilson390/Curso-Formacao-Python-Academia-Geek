"""
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá! Eu sou o/a {nome}.'

@gritar
def orderar(principal, acompanhamento):
    return f"Olá! Eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor."

print(saudacao('Angelina'))

# print(orderar("picanha suina", "feijãoo verde")) #TypeError:


# Utilizando Decoratyor Pattenr==rn

def gritar (funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá! Eu sou o/a {nome}.'

@gritar
def orderar(principal, acompanhamento):
    return f"Olá! Eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor."

print(saudacao('Angelina'))

print(orderar("picanha suina", "feijão verde"))

print(orderar(principal="maminha", acompanhamento="arroz"))
"""

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f"Valor incorreto! Primeiro argumento precisa ser {valor}"
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento("Pizza")
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


#print(soma_dez(10, 12))
#print(soma_dez(1, 21))

print(comida_favorita("Pizza", "Churrasco"))

print(comida_favorita("sanduiche", "Pizza"))