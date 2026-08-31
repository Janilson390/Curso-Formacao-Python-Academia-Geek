# Forma 1 - Importando todo o modulo (não recomendado)
# import random
"""
Ele importa dos as funções, classes e váriaveis de uma vvez e ficam disponíveis na memoria.
O ideal é só importar o que precisa.
"""
# print(dir(random))
""" 
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', 
'_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', 
'_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', 
'_parse_args', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator',
'_urandom', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 
'gauss', 'getrandbits','getstate', 'lognormvariate', 'main', 'normalvariate', 'paretovariate', 
'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 
'uniform', 'vonmisesvariate', 'weibullvariate']

# print(random.random())

# Forma 2 - Imposrtndo só a função
from random import random as rd

for i in range(1, 10):
    print(rd())

"""
from random import random, uniform, randint, choice, shuffle

for i in range(1, 10):
    print(random())

for i in range(10):
    print(uniform(3, 7))

for i in range(10):
    print(randint(3, 61), end=", ")

jogadas = ["pedra", "papel", "tesoura"]

print(choice(jogadas))

print(choice("Geek University"))

cartas = ["K", "Q", "J", "2", "3", "4", "5", "6", "7"]

print(cartas)

shuffle(cartas)

print(cartas)