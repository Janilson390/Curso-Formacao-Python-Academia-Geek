"""
Reduce

Obs 1: Utilizar apartir do módulo 'functools'
Obs 2: Só utilize se realmente precisa dela. Em 99% dos casos, um loop for é mais legível.

Ela funciona assim:
    Passo 1: res1 = f(a1, a2)   -> Aplica a função dos dois primeiros elementos da coleção e q=gaurda o resultado
    Passo 2: res2 = f(res1, a3) -> Aplica a função passando o resultado do passo 1 mais o terceiro e guarda o res. Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resn, an)
"""
from functools import reduce

dados = [1, 2, 3, 4, 5, 6, 7, 8, 9]
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(f"Resultado= {res}")

res = 1
for n in dados:
    res *= n

print(f"Resultado= {res}")
