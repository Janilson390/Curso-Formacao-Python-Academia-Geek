""" 
Generation Function
 - Utilizam yield
 - Podem utilizar o yield múltiplas vezes
 - Quando executada, retona um gerador
 - 

"""

# Exemplo função geradora (Generator Function)
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

gen = conta_ate(10)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)