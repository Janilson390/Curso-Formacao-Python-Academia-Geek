# Função em Python
def funcao(x):
   return 3 * x + 1
print(funcao(4))

# Lambda
lambda x: 3 * x + 1

# Utilizando Lambda
calc = lambda x: 3 * x + 1
print(calc(5))

nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(nome_completo("    JANILSON     ", "Florencio"))
print(nome_completo("Mayara", " freire"))

amar = lambda : "Como não amar lambda?!"
uma  = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6,9))

mais_param = lambda x, y: x * 6 * y

print(mais_param(5, 6))
# print(mais_param(5, 6, 7)) # TypeError

autores = ["Janilson Florencio", "Mayara Freire", "Lara Freire da Silva Forencio", "Anísio Ferreira", "Agata Garcia"]

print(autores)

autores.sort()
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.strip(" ")[-1].lower())
print(autores)

# Função quadrática
# f(x) = a * x ** 2 + b * x + c

def geradora_funcao_quadratica(a, b, c):
   """Retorna a função f(x) = a * x ** 2 + b * x + c

   Args:
       a: Valor de a
       b: Valor de b
       c: Valor de c

   Returns:
       x : Valor de x
   """
   return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(2, 3, -5)(9))