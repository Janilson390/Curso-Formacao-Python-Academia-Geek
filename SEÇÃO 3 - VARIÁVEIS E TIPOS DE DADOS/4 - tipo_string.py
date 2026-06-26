
print('Geek University', type('Geek University'))
print("Geek University", type("Geek University"))
print('''Geek University''', type('''Geek University'''))
print("""Geek University""", type("""Geek University"""))

nome = "Angelina \nJolie"
print(nome, type(nome))
nome = """Angelina
Jolie"""
print(nome, type(nome))

nome = "Angelina \" Jolie"
print(nome, type(nome))

nome = "Angelina Jolie"
print(nome.upper())
print(nome.lower())
print(nome[4:12])
print(nome[4:])
print(nome.split())
print(nome.split()[0])
# COmeçe do primeiro elemento, vá até o último e inverta
print(nome[::-1])  # Inversão de string em método Pythônico

# Remove os espaços em branco iniciais e finais
nome = "  Angelina Jolie  "
print(nome.strip())
