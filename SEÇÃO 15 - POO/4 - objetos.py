
class Cliente:
    contador = 0

    def __gera_id(self):
        self.__id = Cliente.contador + 1
        Cliente.contador = self.__id

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__gera_id()

    def __get_id(self):
        return f"{self.__id}"
    
    def get_cliente(self):
        return f"{self.__get_id()} {self.__nome} - {self.__cpf}"
    

class ContaCorrente:

    contador = 4999

    def __gera_id(self):
        self.__id = ContaCorrente.contador + 1
        ContaCorrente.contador = self.__id

    def __init__(self, cliente, limite, saldo):
        self.__cliente = cliente
        self.__limite = limite
        self.saldo = saldo
        self.__gera_id()

    def get_conta(self):
        print("********** Conta Corrente ************")
        print(f"Nº {self.__id}")
        print(f"Cliente {self.__cliente.get_cliente()}")
        print(f"Limite= {self.__limite} Saldo= {self.saldo}")
        

cl1 = Cliente("Janilson Florencio da Silva", "123.456.789-00")

print(cl1.get_cliente())

cc1 = ContaCorrente(cl1, 2000, 500)

cc1.get_conta()