import math as m

def area(r):
    """Calcula a área de um círculo com raio 'r'

    Args:
        r : raio

    Returns:
        float : Valor da área
    """
    return m.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma normal
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Map
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - map e Lambda
print(list(map(lambda r: m.pi * (r ** 2), raios)))

cidade= [('Berli', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Tokio', 27)]

print(cidade)

# f = 9/5 * c + 32
# lambda

print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidade)))