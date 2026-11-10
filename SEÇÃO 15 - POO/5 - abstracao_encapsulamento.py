class  Conta:

    contador = 4999

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
        print(f"Titular: {self.__titular}! Saldo de {self.__saldo} como limite de {self.__limite}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print(f"O valor precisa ser positivo!")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print(f"Saldo insufciente!")
        else:
            print(f"O valor deve ser positivo!")

    def transferencia(self, valor, conta_destino):
        #1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10
        #2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor

# Testando
conta1 = Conta("Janilson Florencio", 1000, 1000)
conta1.extrato()

conta2 = Conta("Mayara Freire", 500, 1000)
conta2.extrato()

conta1.transferencia(500, conta2)

conta1.extrato()
conta2.extrato()

conta1.depositar(-100)
conta1.depositar(250)

conta1.extrato()


conta2.sacar(250)
conta2.extrato()