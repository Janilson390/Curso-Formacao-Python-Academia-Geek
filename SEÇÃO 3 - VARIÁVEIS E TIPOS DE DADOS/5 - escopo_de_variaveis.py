# Variável de escopo global
numero = 9
print(numero)

if numero > 10:
    novo = 20  # Variável de escopo local
    numero = novo

print(novo)
