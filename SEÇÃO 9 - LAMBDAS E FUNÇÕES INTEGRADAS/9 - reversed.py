lista = [1, 2, 3, 4, 5, 6]
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))

for letra in reversed("Geek University"):
    print(letra, end=" ")

print("\n")
print("".join(list(reversed("Geek University"))))
print("Geek University"[::1])

for n in reversed(range(1, 10)):
    print(n, end="")