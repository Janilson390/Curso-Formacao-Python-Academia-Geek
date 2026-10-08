"""
1. Crie um programa que.
    a) Crie/abra um arquivo texto de nome “arq.txt”
    b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere “0”.
    c) Feche o arquivo
    d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados.

import os


# os.mkdir("SEÇÃO 12 - LEITURA E ESCRITA DE ARQUIVOS\\exercicio")
# os.chdir("exercicio")
# print(os.getcwdb())
# with open("")

with open("arq.txt", "w") as arquivo:
    while True: 
        caracter = input("Digite qualquer coisa: ")
        if caracter != "0":
            arquivo.write(caracter + "\n")
        else:
            break 

with open("arq.txt", "r") as arquivo:
    print(arquivo.read())

"""

"""
2. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são
vogais e quantas são consoantes.

import os

vogais: int = 0
consoantes: int = 0
arquivo: str = input("Digite um arquivo: ")

try:
    with open(arquivo, "r") as arq:
        linhas = arq.readlines()

        print(linhas)

        for linha in linhas:
            #print(linha.replace("\n", "").lower())
            vogais += len([v for v in linha.replace("\n", "").lower() if v in 'aeiou'])
            consoantes += len([c for c in linha.replace("\n", "").lower() if c not in 'aeiou'])

            #if linha.replace("\n", "").lower() in ["a", "e", "i", "o", "u"]:
            #    vogais = vogais + 1
            #else:
            #    consoantes = consoantes + 1

    print(f"Vogais: {vogais}")
    print(f"Consoantes: {consoantes}")
except FileNotFoundError as e:
    print(f"Arquivo não encontrado! {e}")
except FileExistsError as e:
    print(f"Arquivo não existe! {e}")
"""

"""
3. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este
arquivo possui.
"""

import os

arquivo: str = input("Digite um arquivo: ")

try:
    with open(arquivo, "r") as arq:
        linhas = len(arq.readlines())

        print(f"Linhas {linhas}")
except FileNotFoundError as e:
    print(f"Arquivo não encontrado! {e}")
except FileExistsError as e:
    print(f"Arquivo não existe! {e}")