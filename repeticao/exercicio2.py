"""
Escreva um programa que leia valores numéricos inteiros e
totalize separadamente os positivos e os negativos até que o usuário digite 0.
Ao final, mostre
na tela esses dois totais.
"""

N = float(input("informe um n: "))

positivo = N
negativo = N

while N != 0:
    N = float(input("informe um n: "))
    
    if N > 0:
        positivo += N

    else:
        negativo += N

print("valores positivos: ", positivo)
print("valores negativos: ", negativo)
