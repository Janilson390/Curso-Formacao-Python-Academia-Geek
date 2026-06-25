"""
Tipos numéricos

>>> 5 / 2
2.5
>>> 5 //2
2
>>> 3 ** 3
27
>>> 2 ** 8
256
>>> 2 ** 63
9223372036854775808
>>>
>>>
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>>
>>>
>>> 1000
1000
>>> 1000000
1000000
>>> 1_000_000
1000000
>>> num = 43
>>>
>>> dir(num)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__',
    '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
"""
num = 43

print(num + 3)

print(num / 2)

print(num // 2)

num += 2

print(num)

# Todas as funções que podemos utilizar com essa variável
print(dir(num))
print(num.__add__(3))

print(type(num))
print(type(3.0))

num = 1_000_000_000
print(num)
