"""
1. Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro.

2. Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 20204”.

3. Faça um programa que tenha uma função que receba uma lista de inteiros e retorne o maior valor.
"""


def dobro(numero: int) -> int:
    return numero * 2


def formata_data(data: str) -> None:
    dia, mes, ano = str(data).split("/")
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    return f"{dia} de {meses[int(mes) - 1]} de {ano}"


def maior_valor(lista: list[int]) -> int:
    return max(lista)


if __name__ == '__main__':
    valor: int = 4
    print(dobro(valor))
    data: str = "25/04/1988"
    print(formata_data(data))
    lista: list[int] = [1, 2, 3, 4]
    print(maior_valor(lista))
