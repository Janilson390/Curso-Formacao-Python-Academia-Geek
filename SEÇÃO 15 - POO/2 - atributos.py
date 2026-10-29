
# Classe com os atributos publicos
class Lampada:
    
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

# Classe como os atributos privados
class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo

class Produto:
    
    # Atributos de classes
    imposto = 1.50
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        Produto.contador = self.id

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.__email = email
        self.__senha = senha

    def mostra_email(self):
        print(self.__email)

    def mostra_senha(self):
            print(self.__senha)
    

class teste:
    # self é um convenção. É o coreto. 
    # O exemplo é pra mostar que pode ser qualquer coisa
    def __init__(cerveja, num1, num2):
        cerveja.num1 = num1
        cerveja.num2 = num2


usr = Usuario("Janilson", "janilson@teste.net", "123456")

print(usr.nome)
# print(usr.__email) #AttributeError. O atributo é privado
# print(usr.__senha) #AttributeError. O atributo é privado
usr.mostra_email()
usr.mostra_senha()

prd1 = Produto("PlayStation 5", "Video Game", "R$ 4.500,00")
prd2 = Produto("Arroz", "Alimento", "R$ 5,99")

print(f"Id= {prd1.id}, Nome= {prd1.nome}, Descrição= {prd1.descricao}, Valor= {prd1.valor}")
print(f"Id= {prd2.id}, Nome= {prd2.nome}, Descrição= {prd2.descricao}, Valor= {prd2.valor}")

# Atributo em tempo de execução
prd2.peso = "1 Kg"

print(f"Id= {prd2.id}, Nome= {prd2.nome}, Descrição= {prd2.descricao}, Valor= {prd2.valor}, Peso= {prd2.peso}")
#print(f"Id= {prd1.id}, Nome= {prd1.nome}, Descrição= {prd1.descricao}, Valor= {prd1.valor}, Peso= {prd1.peso}") # O atributo 'peso', não existe para esse instância


# Deletando Atributos

print(prd2.__dict__)

del prd2.peso

print(prd2.__dict__)