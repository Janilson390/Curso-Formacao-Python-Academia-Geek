# len() -> retorna o tamanho de um iterável
print("FUNÇÃO len()")
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({"a":1, "b":2, "c":3, "d":4, "e":5}))
print(len({"a":1, "b":2, "c":3, "d":4, "e":5}))
# abs() -> retorna o valor absoluto de um número
print("FUNÇÃO abs()")
print(abs(5))
print(abs(-5))
print(abs(-3.6))
print(abs(3.6))
# sum() -> retorna a soma dos valores de um iterável
print("FUNÇÃO sum()")
print(sum([1, 2, 3, 4, 5]))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(sum({"a":1, "b":2, "c":3, "d":4, "e":5})) 
print(sum({"a":1, "b":2, "c":3, "d":4, "e":5}.values()))
# round() -> retorna o valor arredontado de um valor, após as casas decimais
print("FUNÇÃO round()")
print(round(5.2))
print(round(-5.5))
print(round(5.5))
print(round(3.6))
print(round(3.1235, 2))
print(round(3.62352356, 1))