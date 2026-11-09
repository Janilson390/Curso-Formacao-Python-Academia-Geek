class Lampada:
    def __init__ (self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

class Usuario:

    contador = 0

    # Método de Classe - métodos estáticos em outras linguagens
    @classmethod
    def conta_usuario(cls):
        print(f"Classe {cls}")
        print(f"Temos {cls.contador} usuários no sistema")

    # Métodos privados
    def __gera_usuario(self):
        return self.__email.split("@")[0]

    # Método Estático
    @staticmethod
    def definicao():
        return  'UXRLOP6598'

    # Métodos de Instância
    def __init__(self, nome, sobrenome, email,senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__sobrenome = sobrenome
        Usuario.contador = self.__id
        print(f"Usuário criado: {self.__gera_usuario()}")


    def __correr__(self, metros):
        print(f"{self.__nome} está correndo {metros} metros!")

    def nome_completo(self):
        print(f"{self.__nome} {self.__sobrenome}")

"""
p1 = Produto("Play5", "Console de video-game", 4500)

print(p1.desconto(10))
print(p1.desconto(30))
print(p1.desconto(50))

usr1 = Usuario("Janilson", "Florencio da Silva", "janilson@teste.com", "654321")

usr1.nome_completo()

print(Usuario.nome_completo(usr1))
"""

usr1 = Usuario("Janilson", "Florencio da Silva", "janilson777@teste.com", "654321")

Usuario.conta_usuario() # Certo
usr1.conta_usuario() # Errado

#print(usr1.__gera_usuario()) # AttributeError

print(Usuario.definicao())

print(usr1.definicao())
        