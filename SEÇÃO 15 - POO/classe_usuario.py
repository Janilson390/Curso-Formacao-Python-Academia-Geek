
class Usuario:
    
    def __init__(self, nome, email, senha):
        # Atributos públicos
        self.nome = nome
        self.email = email

        # Atributo privado
        self.__senha = senha

    # Método público para consultar o usuário
    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")

    # Método público para validar a senha
    def validar_senha(self, senha):
        return self.__senha == senha

    # Método público para alterar a senha
    def alterar_senha(self, senha_atual, nova_senha):
        if self.__senha == senha_atual:
            self.__senha = nova_senha
            return True

        return False


# Instanciando um objeto da classe Usuario
usuario = Usuario(
    nome="Janilson",
    email="janilson@email.com",
    senha="123456"
)

# Acessando atributos públicos
print(usuario.nome)
print(usuario.email)

# Apresentando os dados
usuario.apresentar()

# Validando a senha
if usuario.validar_senha("123456"):
    print("Senha válida!")
else:
    print("Senha inválida!")

# Alterando a senha
if usuario.alterar_senha("123456", "654321"):
    print("Senha alterada com sucesso!")
