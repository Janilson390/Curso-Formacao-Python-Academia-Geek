class Pessoa:

    def __init__(self, nome:str, sobrenome:str, cpf:str) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self) -> str:
        return f"{self.__nome} {self.__sobrenome} - CPF: {self.__cpf}"


class Cliente(Pessoa):
    
    def __init__(self, nome, sobrenome, cpf, renda: float):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):

    def __init__(self, nome:str, sobrenome:str, cpf:str, matricula:str):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f"Funcionario: {self.__matricula} {super().nome_completo()}"


cliente1 = Cliente("Janilson", "Florencio", "456.6987.236.01", 8000)
funcionario1 = Funcionario("Mayara", "Freire", "987.456.123-99", "2006987569-01")

print(cliente1.nome_completo())
print(funcionario1.nome_completo())