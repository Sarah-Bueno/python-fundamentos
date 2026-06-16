"""
Escreva um programa que apresente todos os valores inteiros
divisíveis por 5, situados no intervalo fechado [Min, Max], em que Min e Max são fornecidos pelo
usuário. É obrigatório que o valor Max seja maior que Min e, se isso não ocorrer, o programa
deve exibir uma mensagem de aviso ao usuário e inverter os valores.
"""
MIN = int(input("informe um valor menor: "))
MAX = int(input("informe um valor maior: "))


if MAX < MIN:
    print("o máximo é menor que o mínimo , encerrando")

else:
    for i in range (MIN, MAX + 1):
      if i % 5 == 0:
          if MAX > MIN:
              print(i)
