import os
import tempfile

print(os.chdir("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS"))
print(os.getcwd())
print(os.path.exists('3 - with.py'))
print(os.path.exists('10 - outra.py'))

# Absoluto
print(os.path.exists('D:\\Documents\\Cursos\\Curso-Formacao-Python-Academia-Geek\\main.py'))

# Relativo
print(os.path.exists('..\\main.py'))

# Criando arquivos
# Só funciona no POSIX (Linus e Mac OS)
#os.mknod("arquivo.txt")
# No Windows, tem que usar o open()

with open("arquivo.txt", "w") as arquivo:
    pass # QUando não quero fazer nada no bloco, uso a palavra pass

# Criando um diretório
#os.mkdir("GEEK") # Caso já exista, dá o erro FileExistsError

#os.makedirs("GEEK\\University\\aula1", exist_ok=True) # a opção exist_ok ignora caso o diretório já exista.

# Renomear os diretórios
#os.rename('GEEK', 'geek')

#os.rename('geek\\University\\aula1\\arquivo.txt', 'geek\\University\\aula1\\arquivos.txt')

# Deletar arquivos
# CUIDADO! Apagando o arquivo, ele é excluído permanente

#os.remove('geek\\University\\aula1\\arquivos.txt')

# Deletar diretórios
#os.rmdir('geek\\University\\aula1')
#os.removedirs('geek\\University')

# Diretório temporário
"""
with tempfile.TemporaryDirectory() as tmp:
    print(f"Diretório temporário em {tmp}")
    with open(os.path.join(tmp, "arquivo-temp.txt"), 'w') as arquivo:
        arquivo.write("Geek University\n")
    input()
"""

# Arquivo temporário
"""
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n') 
    tmp.seek(0)
    print(tmp.read())
"""

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University')
print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()