class Animal:
    def __init__(self, nome:str):
        self.__nome:str = nome

    def cumprimentar(self) -> str:
        return(f"Olá! Eu sou {self.__nome}")

class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self) -> str:
        return(f"Olá! Eu sou {self._Animal__nome} da agua!")

    def nadar(self) -> str:
        return(f"Olá! Eu sou {self._Animal__nome} e estou nadando!")

class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self) -> str:
        return(f"Olá! Eu sou {self._Animal__nome} da Terra!")

    def andar(self) -> str:
        return(f"Olá! Eu sou {self._Animal__nome} e estou andando!")

class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)
    
if __name__ == "__main__":
    baleia = Aquatico("Wally")
    print(baleia.cumprimentar())
    print(baleia.nadar())

    tatu = Terrestre("Fuleco")
    print(tatu.cumprimentar())
    print(tatu.andar())

    feet = Pinguim("Happy Feet")
    print(feet.cumprimentar())
    print(feet.andar())
    print(feet.andar())

    """"
    Primeira Execução

    Olá! Eu sou Wally da agua!
    Olá! Eu sou Wally e estou nadando!
    Olá! Eu sou Fuleco da Terra!
    Olá! Eu sou Fuleco e estou andando!
    Olá! Eu sou Happy Feet da agua!
    Olá! Eu sou Happy Feet e estou andando!
    Olá! Eu sou Happy Feet e estou andando!

    Segunda Execução

    Olá! Eu sou Wally da agua!
    Olá! Eu sou Wally e estou nadando!
    Olá! Eu sou Fuleco da Terra!
    Olá! Eu sou Fuleco e estou andando!
    Olá! Eu sou Happy Feet da Terra!
    Olá! Eu sou Happy Feet e estou andando!
    Olá! Eu sou Happy Feet e estou andando!
    """
    print(f"feet é intancia de Pinguim? {isinstance(feet, Pinguim)}")
    print(f"feet é intancia de Aguatico? {isinstance(feet, Aquatico)}")
    print(f"feet é intancia de Terrestre? {isinstance(feet, Terrestre)}")
    print(f"feet é intancia de Animal? {isinstance(feet, Animal)}")
    print(f"tatu é intancia de Aquatico? {isinstance(tatu, Aquatico)}")
    print(f"tatu é intancia de Object? {isinstance(feet, object)}")