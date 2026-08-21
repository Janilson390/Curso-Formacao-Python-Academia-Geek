"""
max() -> Retorna o maior valor de um iterável ou de dois ou mais elementos
min() -> Retorna o menor valor de um iterável ou de dois ou mais elementos

lista = [5,69,871,254,632,989,2,6,7,125]
tupla = (5,69,871,254,632,989,2,6,7,125)
conjunto = {5,69,871,254,632,989,2,6,7,125}
dicionario = {"a": 5, "b":69, "c":871, "t":254, "z":632, "f":989, "g":2, "h":6, "i":7, "j":125}

print(f"Na lista, maior valor é {max(lista)} e o menor valor é {min(lista)}")
print(f"Na tupla, maior valor é {max(tupla)} e o menor valor é {min(tupla)}")
print(f"No conjunto, maior valor é {max(conjunto)} e o menor valor é {min(conjunto)}")
# print(max(dicionario.values()))
print(f"No dicionário, a maior chave é \"{max(dicionario)}\" e o maior valor é {max(dicionario.values())}. Já a menor chave é \"{min(dicionario)}\" e o  menor valor é {min(dicionario.values())}")

val1 = int(input("Digite o 1º valor "))
val2 = int(input("Digite o 2º valor "))

print(f"O maior valor é {max(val1, val2)}")
print(f"O menor valor é {min(val1, val2)}2")

print(max(4, 67, 0))
print(min(4, 67, 0))

print(max('a','ab','adc','adca'))
print(min('a','ab','adc','adca'))

print(max('Geek University'))
print(min('Geek University'5))
"""
nomes = ["Arya", "Samson", "Dora", "Tim", "Olivander"]
print(max(nomes))
print(min(nomes))

print(max(nomes, key= lambda nome: len(nome)))
print(min(nomes, key= lambda nome: len(nome)))


musicas = [
    {"titulo":"Jerusalém", "tocou":5},
    {"titulo":"Tem sabor de mel", "tocou":1},
    {"titulo":"Meus próprios meios", "tocou":3},
    {"titulo":"Eu navegarei", "tocou":9},
    {"titulo":"Eis que estou a porta e bato", "tocou":2}
]

print(f"As musicas mais tocadas -> {max(musicas, key=lambda musica: musica["tocou"])}\n")

print(f"As musicas menos tocadas -> {min(musicas, key=lambda musica: musica["tocou"])}")

print(f"As musicas mais tocadas -> {max(musicas, key=lambda musica: musica["tocou"])["titulo"]}\n")

print(f"As musicas menos tocadas -> {min(musicas, key=lambda musica: musica["tocou"])["titulo"]}")

max = 0
for musica in musicas:
    if musica["tocou"] > max:
        max = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == max:
        print(musica["titulo"])

min = 999999
for musica in musicas:
    if musica["tocou"] < min:
        min = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == min:
        print(musica["titulo"])