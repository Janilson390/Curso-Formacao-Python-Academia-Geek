class Pessoa:

    def __init__(self, nome, email, data_nascimento):
        self.__nome = nome
        self.__email = email
        self.__data_nascimento = data_nascimento

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    # Getters
    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_data_nascimento(self):
        return self.__data_nascimento

    # Métodos
    def imprimir(self):
        print(f"Nome: {self.get_nome()}; Email: {self.get_email()}; Data de Nascimento: {self.get_data_nascimento()}")

if __name__ == "__main__":

    # Teste
    ps1 = Pessoa("Janilson Florencio", "janilson698@teste.ai", "04/08/1987")

    ps1.imprimir()

    ps1.set_data_nascimento("08/09/1986")

    ps1.imprimir()















