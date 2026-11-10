from exercicio1 import Pessoa

class Agenda:

    def __init__(self):
        self.__contados: list[Pessoa] = []

    @property
    def contatos(self) -> list[Pessoa]:
        return self.__contados

    def armazenar_contatos(self, contato: Pessoa) -> None:
        self.contatos.append(contato)

    def remover_contato(self, contato: Pessoa) -> None:
        self.contatos.remove(contato)

    def buscar_contato(self, nome: str) -> None:
        for indice, contato in enumerate(self.__contados):
            if contato.get_nome() == nome:
                print(f"O Contato {nome} está na posiçao {indice}")

    def imprimir_agenda(self) -> None:
        for contato in self.contatos:
            contato.imprimir()

    def imprimir_contato(self, indice: int) -> None:
        self.contatos[indice].imprimir()

if __name__ == "__main__":
    contato1: Pessoa = Pessoa("Janilson Florencio", "janilson698@teste.ai", "04/08/1987")
    contato2: Pessoa = Pessoa("Mayara Freire", "mayara654@teste.ai","06/09/1989")
    contato3: Pessoa = Pessoa("Lara Freire", "lara.freire@teste.ai", "12/02/2013")

    agenda: Agenda = Agenda()

    agenda.armazenar_contatos(contato1)
    agenda.armazenar_contatos(contato2)
    agenda.armazenar_contatos(contato3)

    agenda.imprimir_agenda()
    agenda.buscar_contato("Lara Freire")
    agenda.imprimir_contato(2)
    agenda.remover_contato(contato1)
    agenda.imprimir_agenda()