class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f"O {self.__nome} está comendo ...")
    
    def falar(self):
        print("A classe filha precisa implementar esse método!") 

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def comer(self):
            print(f"O {self._Animal__nome} está roendo um osso!")
        
    def falar(self):
        print(f"O {self._Animal__nome} está latindo!") 

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def comer(self):
            print(f"O {self._Animal__nome} está comendo um peixe!")
        
    def falar(self):
        print(f"O {self._Animal__nome} está miando!")

class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def comer(self):
            print(f"O {self._Animal__nome} está comendo um queijo!")
    
    def falar(self):
         pass
        
if __name__ == "__main__":
     gato1 = Gato("Felix")
     gato1.comer()
     gato1.falar()

     cachorro1 = Cachorro("Pluto")
     cachorro1.comer()
     cachorro1.falar()

     rato1 = Rato("Mickey")
     rato1.comer()
     rato1.falar()