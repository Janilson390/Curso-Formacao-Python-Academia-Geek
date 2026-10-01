"""
# Maneira tradicional
arquivo = open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\novo.txt", 'w')

arquivo.write("É muito bom aprender Python!\n")
arquivo.write("Dá pra fazer muito com isso.\n")
arquivo.write("Espero chegar ao cargo de Engenheiro de Dados com isso.\n")

arquivo.close()


# Maneira Pythônica
with open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\outro.txt", 'w') as arquivo:
    arquivo.write("É muito bom aprender Python!\n")
    arquivo.write("Dá pra fazer muito com isso.\n")
    arquivo.write("Espero chegar ao cargo de Engenheiro de Dados com isso.\n")
    print(f"O arquivo está aberto? {"Não" if arquivo.closed else "Sim"}")


print(f"O arquivo está aberto? {"Não" if arquivo.closed else "Sim"}")

with open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\outro.txt", 'w') as arquivo:
    arquivo.write("Dá pra fazer muito com isso.\n")
    # arquivo.write(560) TypeError: write() argument must be str, not int
    arquivo.write(str(560))
    

with open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\outro.txt", 'w') as arquivo:
    arquivo.write("Dá pra fazer muito com isso.\n" * 20)
"""

with open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\outro.txt", 'w') as arquivo:
    while True:
        fruta = input("Digite uma fruta: ")
        if fruta != 'sair':
            arquivo.write(f"{fruta}\n")
        else: 
            break
