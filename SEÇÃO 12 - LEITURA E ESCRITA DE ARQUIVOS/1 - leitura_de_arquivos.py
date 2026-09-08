#arquivo = open('D:\\Documents\\Cursos\\Curso-Formacao-Python-Academia-Geek\\SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\texto.txt')

arquivo = open('SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\texto.txt')

print(arquivo)
print(type(arquivo))

# print(arquivo.read())

ret = arquivo.read()

print(ret.split("\n"))