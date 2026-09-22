"""
seek() -> É utilizado para movimentar o cursor pelo arquivo. Seek é procurar

arquivo = open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\texto.txt")

print(arquivo.read())

print(arquivo.read())

arquivo.seek(0)
print(arquivo.read())

arquivo.seek(15)
print("\n",arquivo.read())

arquivo = open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\texto.txt")

# readline() -> Lê o arquivo linha a linha

print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

# ret = arquivo.readline()

# print(type(ret))
# print(ret)

arquivo = open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\texto.txt")

# readlines() -> Coloca todas as linhas do araquivo em uma lista

# print(arquivo.readlines())

linhas = arquivo.readlines()

print(len(linhas))
print(type(linhas))
print(linhas)
"""

# Abrindo um aquivo
arquivo = open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\texto.txt")

# Trabalhando com o arquivo
print(arquivo.read())
print(arquivo.closed)

arquivo.seek(0)

print(arquivo.read(30))

# Fechando um arquivo
arquivo.close()

print(arquivo.closed)

print(arquivo.read())


