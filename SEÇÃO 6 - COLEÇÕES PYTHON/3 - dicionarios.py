"""
print(type({}))
print(dir({}))

# 1ª forma de declarar
paises = {"br": "Brasil", "eua": "Estados Unidos", "py": "Paraguai"}
print(paises)

# 2ª forma de declarar
paises = dict(br="Brasil", eua="Estados Unidos", py="Paraguai")
print(paises)
print(type(paises))

# Acessando elementos

# 1º Forma de acesso
paises = {"br": "Brasil", "eua": "Estados Unidos", "py": "Paraguai"}
print(paises["br"])
print(paises["py"])
# print(paises["ru"])  # Erro pq não existe

# 2º Forma de acesso (recomendado)
print(paises.get("br"))
print(paises.get("py"))
print(paises.get("ru"))  # Não dá erro. Retorna None

# Tipo None
numeros = None
print(numeros)
print(type(numeros))

numeros = 1.45, 4.56, 8.6
print(numeros)
print(type(numeros))

paises = {"br": "Brasil", "eua": "Estados Unidos", "py": "Paraguai"}
pais = paises.get("py", "País inexistente")
# pais = paises.get("ru", "País inexistente")

if pais:
    print(f"Encontrei o país {pais}!")
else:
    print(f"Não encontrei o país! {pais}")

# Verificando se uma chave está no dicionário.
# Ele verifica só a chave, não o valor.
paises = {"br": "Brasil", "eua": "Estados Unidos", "py": "Paraguai"}

print("br" in paises)
print("ru" in paises)
print("Paraguay" in paises)

if "ru" in paises:
    russia = paises["ru"]

print(type(paises["br"]))

localidades = {
    (35.6895, 39.6917): "Escritório em Tókio",
    (40.7128, 35.3265): "Escritório em Nova York",
    (37.9698, 41.6989): "Escritório em São Paulo",
}

print(localidades)
print(type(localidades))

# Adicionando elementos em um dicionário
receita = {"jan": 100, "fev": 120, "mar": 300}
print(receita)
# Forma1 (mais comum)
receita["abr"] = 350
print(receita)

# Forma 2
novo_valor = {"mai": 500}
receita.update(novo_valor)
print(receita)

receita.update({"jun": 600})
print(receita)

# Atualizando elementos em um dicionário
receita["abr"] = 700
print(receita)

receita.update({"jan": 1000})
print(receita)

# Não existe em dicionários chaves repetidas. Ele sobrescreve a chave existente.
receita2 = {"jan": 100, "jan": 1500, "fev": 120, "mar": 300}
print(receita2)

# Remover elementos de um dicionário
receita = {'jan': 1000, 'fev': 120, 'mar': 300,
           'abr': 700, 'mai': 500, 'jun': 600}
print(receita)

# Forma 1 (mais comum)
receita.pop("jan")
print(receita)

# Forma 2
del receita['jun']
print(receita)

# Métodos de dicionários
d = dict(a=1, b=2, c=3)
print(d)

d.clear()
print(d)

# Copiando um dicionário
# Deep Copy
d = dict(a=1, b=2, c=3)
print(d)

novo = d.copy()
print(novo)

novo["d"] = 4
print(d)
print(novo)

# Shallow Copy
d = dict(a=1, b=2, c=3)
print(d)

novo = d
print(novo)

novo["d"] = 4
print(d)
print(novo)
"""
# Maneira não usual de criação de dicionário
# fromkeys recebem dois parâmetros: um interável (gerar a(s) chave(s) do dicionário) e um valor (será o valor atribuido a chave)
outro = {}.fromkeys("a", "b")

print(outro)
print(type(outro))

outro2 = {}.fromkeys(["nome", "pontos", "email", "profile"], "desconhecido")

print(outro2)
print(type(outro2))

veja = {}.fromkeys("teste", "valor")
print(veja)
print(type(veja))

veja = {}.fromkeys(range(1, 11), "novo")
print(veja)
print(type(veja))
