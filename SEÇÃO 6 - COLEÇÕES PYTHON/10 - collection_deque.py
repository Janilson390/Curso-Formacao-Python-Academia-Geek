from collections import deque

# Criando Deques
deq = deque("geek")

print(deq)

# Adicionando elementos no deque
deq.append("y")
print(deq)

deq.appendleft("k")
print(deq)

# Removendo elementos
print(deq.pop())
print(deq)

print(deq.popleft())
print(deq)
