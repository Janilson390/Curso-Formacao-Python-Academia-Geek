"""
Estruturas lógicas: AND, OR, NOT e IS

Operadores unários: not
Operadores binários: and, or e is

"""
ativo = True
logado = False

if ativo and logado:  # As duas condições tem que ser verdadeiras
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu email!")

if ativo or logado:  # Uma das condições tem que ser verdadeira
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu email!")

if not ativo:  # O valor da condição é invertido. Forma Pythônica de escrever
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu email!")

if ativo is True:  # O valor da condição é invertido
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu email!")

# Testando mais o IS
print(ativo is True)
print(ativo is False)

# IS integrado a outras funções
nome = "geek"
nome_variavel = f"{nome=}".split("=")[0]
print("O valor da variável {0} é MAIUSCULO: {1}".format(
    nome_variavel, nome.isupper()))
print("O valor da variável {0} é MAIUSCULO: {1}".format(
    nome_variavel, nome.islower()))
print(f"Titulo: {nome.title()}")
print(nome.title().istitle())
print(f"Valor Janilson é Numérico: {"Janilson".isnumeric()}")
print(f"Valor Janilson é String: {"Janilson".isalpha()}")
