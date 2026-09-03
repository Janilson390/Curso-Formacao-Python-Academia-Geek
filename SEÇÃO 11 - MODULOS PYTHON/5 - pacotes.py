""" 
from geek import geek1, geek2

from geek.university import geek3, geek4

print(geek1.funcao(5, 6))
print(geek1.pi)

print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())
print(geek4.funcao4())

from geek.geek1 import funcao

print(funcao(5, 9))
"""

from geek.geek1 import *

print(funcao(5, 9))
print(pi)

