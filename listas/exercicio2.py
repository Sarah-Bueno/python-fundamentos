"""
Escreva um programa que leia do teclado dois números
inteiros nA e nB e leia também duas listas denominadas A e B com os tamanhos nA e nB,
respectivamente. Na leitura de cada uma das listas é obrigatório que não sejam aceitos valores
repetidos. Em seguida, o programa deve juntar as duas em uma única lista R (resultante),
tomando o cuidado de que R não tenha valores duplicados.
"""
nA = int(input("Tamanho da lista A: "))
nB = int(input("Tamanho da lista B: "))

A = []
B = []

print("\nDigite os valores da lista A:")
for i in range(nA):
    x = int(input())
    if x not in A:
        A.append(x)
    else:
        print("Número repetido! Não será adicionado.")

print("\nDigite os valores da lista B:")
for i in range(nB):
    x = int(input())
    if x not in B:
        B.append(x)
    else:
        print("Número repetido! Não será adicionado.")

R = list(set(A + B))

print("\nLista resultante:", R)
