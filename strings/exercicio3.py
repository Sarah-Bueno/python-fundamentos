"""
Escreva um programa que receba uma palavra e devolva
quantas letras diferentes essa palavra contém.
"""
s = input("Digite a palavra: ")

diferentes = ""

for letra in s:
    if letra not in diferentes:
        diferentes += letra

print(len(diferentes))
