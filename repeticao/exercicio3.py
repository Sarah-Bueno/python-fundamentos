"""
Escreva um programa que calcule os N primeiros termos
de uma PG com razão R e o primeiro termo P1 fornecidos pelo usuário. Também deve ser
calculada e apresentada a soma desses N termos.
"""

P1 = int(input("informe um P1: "))
PG = int(input("informe um PG: "))
R = int(input("informe um R: "))

soma = 0

for i in range(P1, PG + 1, R):
    soma += i
    print(i)
print("a soma da PG é: ", soma)
