""Escreva um programa que receba um texto em uma string
ENTRADA e devolva, em uma string SAIDA, esse mesmo texto, tendo sido eliminados todos
os espaços em branco."""

entrada = input("Digite algo: ")
nova = ""

for letra in entrada:
    if letra != " ":
        nova += letra


print(nova)
