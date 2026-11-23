class Animal:
    
    def __init__(self, nome:str, especie:str):
        self.__nome:str = nome
        self.__especie:str = especie

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome:str) -> None:
        self.__nome = nome

    @property
    def especie(self) -> str:
            return self.__especie
    
    @especie.setter
    def nome(self, especie:str) -> None:
        self.__especie = especie

    def som(self, som:str):
        print(f"O {self.__nome} faz {som}!")

class Gato(Animal):

    def __init__(self, nome, especie, raca:str):
        #Animal.__init__(self, nome, especie) #Incomum
        super().__init__(nome, especie) #Comum
        self.__raca:str = raca

    @property
    def raca (self) -> str:
        return self.__raca
    
    @raca.setter
    def raca (self, raca:str) -> None:
        self.__raca = raca

if __name__ == "__main__":
    gato1 = Gato("Bichano", "Felino", "Siames")

    gato1.som("miaaaaau")