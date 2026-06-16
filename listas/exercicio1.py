"""
Escreva um programa que leia do teclado duas listas com
tamanho 10, com números inteiros. Em seguida, o programa deve
juntar as duas listas em uma única com o tamanho 20.
"""

A = []

for i in range(10):
    V = int(input("informe 10 elementos: "))
    A.append(V)
    
B = []

for i in range(10):
    V1 = int(input("informe 10 elementos: "))
    B.append(V1)
    
SOMA = A + B

print(SOMA)
