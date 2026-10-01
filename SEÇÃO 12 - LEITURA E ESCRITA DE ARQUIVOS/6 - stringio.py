# StringIO -> Lê e cria um arquivo em memoria

from io import StringIO

mensagem = "Essa é uma mensagem!"

arquivo = StringIO(mensagem)
# É a mesma coisa de -> arquivo = open("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\arquivo.txt", 'w')

print(arquivo.read())

arquivo.write("Mais uma mensagem")

arquivo.seek(0)

print(arquivo.read())

print(f"O arquivo está aberto? {"Não" if arquivo.closed else "Sim"}")

arquivo.close()

print(f"O arquivo está aberto? {"Não" if arquivo.closed else "Sim"}")


