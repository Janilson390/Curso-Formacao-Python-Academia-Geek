"""
Criando sua propria versão de loop

# O normal

nome = 'geek'
for letra in nome:
    print(letra)

# Por trás dos panos
itl = iter(nome)

print(next(itl))
print(next(itl))
print(next(itl))
print(next(itl))
# print(next(itl)) # StopIteration
"""
def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for([1, 2, 3, 4, 6])

nome = 'Geek University'

meu_for(nome)



