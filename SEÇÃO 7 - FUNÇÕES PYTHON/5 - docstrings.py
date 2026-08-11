def oi():
    """
    Uma função que retorna a string Oi!
    """
    return "Oi!"


def exponencial(numero, potencia=2):
    """Função que retorna por padrão o quadrado de um 'numero' ou 'numero' á 'potência informada!'

    Args:
        numero (int): _Número que desejamos gerar o exponencial
        potencia (int, optional): Número que queremos potencializar. Defaults to 2.

    Returns:
        int : resultado da exponenciação
    """
    return numero ** potencia


print(oi.__doc__)
print(exponencial.__doc__)
