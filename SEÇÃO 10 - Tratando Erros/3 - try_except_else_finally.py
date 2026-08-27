"""
try: 
    num = int(input("Informe um número: "))
except ValueError:
    print("Você não digitou um número válido")
else:
    print(f"Você digitou o número {num}")
finally:
    print(f"Obrigado amigo!")
# Você é responsável pelo seu código. Trate os seus erros.

def dividir(a, b):
    try:
        return int(a) / int(b)
    except TypeError as e:
       print(f"Valores incorretos! {e}")
    except ZeroDivisionError as e:
        print(f"Impossível dividir por 0! {e}")


# BONUS - DEBUGANDO COM PDB
# Comandos:
# l - Lista onde estamos no código
# n - Próxima linha
# p - Imprime uma vaviável que passamos
# c - Continua a execução - finaliza o debugging

import pdb

def dividir(a, b):
    try:
        pdb.set_trace()
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError, TypeError) as e:
       return f"Ocorreu um problema! {e}"

def dividir(a, b):
    try:
        import pdb; pdb.set_trace() # Importando o pdb no meio do código, debugamos somente o que queremos. Depois de utilizado, podemos descartar. 
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError, TypeError) as e:
       return f"Ocorreu um problema! {e}"
"""
def dividir(a, b):
    try:
        breakpoint() # A partit do python 3.7, o pdb foi incorporado na função built-in breakpoint() 
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError, TypeError) as e:
       return f"Ocorreu um problema! {e}"
    
num1 = input("Digite o 1º valor ")
num2 = input("Digite o 2º valor ")

print(f"O valor da divisão é {dividir(num1, num2)}")
