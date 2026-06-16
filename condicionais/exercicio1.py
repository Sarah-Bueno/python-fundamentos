"""
Escreva um programa que leia o nome de um lutador e
seu peso. Em seguida, informe a categoria a que pertence o lutador, conforme o quadro abaixo
(note que o quadro foi criado para efeito deste exercício e não condiz com qualquer categoria
de luta). A saída do programa deve exibir na tela uma frase com o padrão descrito a seguir:

Peso fornecido: 73.4
Frase a ser exibida: O lutador Pepe Jordão pesa 73,4 kg e se enquadra na categoria Ligeiro
"""

NOME = input("Digite o nome do lutador: ")
P = float(input("Digite o peso do lutador: "))

if P < 65:
    categoria = "Pena"
elif 65 <= P  < 72:
    categoria = "Leve"
elif 72 <= P < 79:
    categoria = "Ligeiro"
elif 79 <= P < 86:
    categoria = "Meio-médio"
elif 86 <= P < 93:
    categoria = "Médio"
elif 93 <= P < 100:
    categoria = "Meio-pesado"
else:
    categoria = "Pesado"

print("O lutador",NOME,"pesa",P,"e se enquadra na categoria",categoria)
