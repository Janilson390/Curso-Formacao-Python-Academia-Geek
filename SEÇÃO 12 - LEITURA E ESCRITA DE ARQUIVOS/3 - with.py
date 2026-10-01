
with open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\texto.txt") as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed)
print(arquivo.readlines())