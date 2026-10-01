""" 
Modos
r -> Abre para leitura
w -> Abre para escrita (sobrescreve caso exista)
x -> Abre para escrita somente se o aquivo não existir
a -> Abre para escrever. Adiciona no final do arquivo caso ele exista


with open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\university.txt", 'x') as arquivo:
    arquivo.write("Geek University!")

# Executando novamente, cai no erro de FileExistsError, pois o mesmo já existe.


# SOLUÇÃO PARA ISSO!

try:    
    with open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\university.txt", 'x') as arquivo:
        arquivo.write("Geek University!")
except FileExistsError:
    print("O arquivo já existe!")
"""

with open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\university.txt", 'a') as arquivo:
    while True:
        fruta = input("Digite uma fruta: ")
        if fruta != 'sair':
            arquivo.write(f"{fruta}\n")
        else: 
            break
