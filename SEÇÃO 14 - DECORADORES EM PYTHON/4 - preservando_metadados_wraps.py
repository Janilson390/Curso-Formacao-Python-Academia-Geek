
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """ Eu sou uma funcao (logar) dentro de outra"""
        print(f'Você está chamado {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b

print(soma(10, 20))
print(soma.__name__)
print(soma.__doc__)

print(help(soma))