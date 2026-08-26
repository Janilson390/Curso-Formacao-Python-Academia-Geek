def colere (texto, cor):
    cores = ("verde", "amarelo", "azul", "branco")
    if type(texto) is not str:
        raise TypeError("O parametro \"texto\" precisa ser uma string!")
    if type(cor) is not str:
        raise TypeError("O parametro \"cor\" precisa ser uma string!")
    if cor.lower() not in cores:
        raise ValueError(f"A cor precisa ser uma destas: {cores}!")

    print(f"O texto {texto} será impresso na cor {cor}!")

# colere("Raposa", "AZUL")
colere("Gato", "preto")
# colere(5, "AZUL")
# colere("Gato", 6.3)

