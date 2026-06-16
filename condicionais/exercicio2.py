"""
Construa um programa que receba o número do cadastro
(inteiro) de três clientes de uma loja e o valor (em reais) que cada um desses clientes pagou por
sua compra. O programa deverá informar:

• o valor total pago pelos três clientes;
• o valor da compra média efetuada;
• o número de cadastro dos clientes que efetuaram compras superiores a 100 reais;
• quantos clientes efetuaram compras inferiores a 50 reais.
"""
C1 = int(input("digite o valor de cadastro 1: "))
C2 = int(input("digite o valor de cadastro 2: "))
C3 = int(input("digite o valor de cadastro 3: "))

V1 = float(input("digite o valor de V1: "))
V2 = float(input("digite o valor de V2: "))
V3 = float(input("digite o valor de V3: "))

VT = V1 + V2 + V3
VM = VT / 3

soma = 0
conta = 0
if V1 > 100:
    conta = C1
if V2 > 100:
    conta = C2
if V3 > 100:
    conta = C3

if V1 < 50:
    soma +=1
if V2 < 50:
    soma +=1
if V3 < 50:
    soma +=1

print("valor total", VT)
print("valor médio" , VM)
print("quantidade de cadastros com compras inferiores a 50 reais:", soma)
print("número de cadastro de compras acima de 100 reais:", conta)
