# Python 2.x
"""
print("Qual o seu nome?")
nome = input()

print("Seja bem-vindo(a) %s" % nome)

print("\nQuual a sua idade?")
idade = input()
print("%s! Você tem %s anos!" % (nome, idade))
"""

# Python 3.x
nome = input("Qual o seu nome?\n")
print("Seja bem-vindo(a) {0}".format(nome))

idade = input("\nQual a sua idade?\n")
print(f"{nome}! Você tem {idade} anos! Você nasceu em {2026 - int(idade)}.")
