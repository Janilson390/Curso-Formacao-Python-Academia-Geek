import os, sys

# getcwd() -> mesmo do pwd
print(os.getcwd())

#chdir([caminho]) -> mesmo do cd
# os.chdir("..")
# print(os.getcwd())

os.chdir("D:\\Documents\\")
print(os.getcwd())

# os.path.isabs([caminho]) -> Checar se um caminho é absoluto ou relativo
print(os.path.isabs("D:\\Documents\\Cursos\\Curso-Formacao-Python-Academia-Geek"))
print(os.path.isabs("D:\\Documents\\..\\.."))

# Para Windowns o caminho fica com a '\' de escape para montar o caminho. Ex: C:\\Documentos\\arquivos\\..
# No Linux e Mac, o caminho fica normal. Ex: /home/arquivos/..

# Identifica o sistema operacional com o modulo os: posix (linux ou mac) ou nt (Windows)
print(os.name)

# Mais detalhado (windows)
print(sys.platform)

#print(os.listdir("D:\\Documents\\Cursos\\Curso-Formacao-Python-Academia-Geek"))
#print(len(os.listdir("D:\\Documents\\Cursos\\Curso-Formacao-Python-Academia-Geek")))

#print(list(os.scandir()))

scanner = os.scandir()
arquivo = list(scanner)

print(arquivo[0].inode())
print(arquivo[0].is_dir())
print(arquivo[0].is_file())
print(arquivo[0].is_symlink())
print(arquivo[0].name)
print(arquivo[0].path)
print(arquivo[0].stat())

print(os.getcwd())

scanner.close()
print(os.getcwd())
