def colere (texto, cor):
    try:
        cores = ("verde", "amarelo", "azul", "branco")
        if cor.lower() not in cores:
            raise ValueError
        print(f"O texto {texto} será impresso na cor {cor}!")
    except ValueError:
        print(f"A cor precisa ser uma destas: {cores}!")
    except TypeError as err:
        if type(texto) is not str:
            print(f"O parametro \"texto\" precisa ser uma string! {err}")
    except:
        if type(cor) is not str:
            print(f"O parametro \"cor\" precisa ser uma string!")


colere("Raposa", "AZUL")
colere("Gato", "preto")
colere(5, "AZUL")
colere("Gato", 6.3)

