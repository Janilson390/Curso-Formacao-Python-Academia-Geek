"""
Utilize o Pip (Python Installer Package)
Onde encontrar pacotes externos: https://pypi.org
exemplo: pip install colorama


# from colorama import init, Fore, Back, Style


init()

print(Fore.RED + "Janilson Florencio")
print(Fore.MAGENTA + "Janilson Florencio")
print(Back.CYAN + "Janilson Florencio")
print(Style.RESET_ALL)
print("Volta ao normal")
"""

import pydf

pdf = pydf.generate_pdf("Geek University")

with open("teste_doc.pdf", "wb") as f:
    f.write(pdf)