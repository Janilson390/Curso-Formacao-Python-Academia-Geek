from collections import namedtuple

# Forma 1
cachorro = namedtuple("cachorro", "idade raca nome")

# Forma 2
cachorro = namedtuple("cachorro", "idade, raca, nome")

# Forma 3
cachorro = namedtuple("cachorro", ["idade", "raca", "nome"])

# Usando

ray = cachorro(idade=2, raca="chow-chow", nome="Ray")
print(ray)
print(type(ray))

print(ray[0])
print(ray[2])

print(ray.idade)
print(ray.raca)
