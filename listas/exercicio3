"""
Uma academia deseja registrar as avaliações físicas realizadas ao longo de uma semana.
Para cada avaliação, o instrutor informa a idade do aluno avaliado. As idades devems er armazenadas em uma lista.
Você deve implementar um programa em Python que leia as idades dos alunos avaliados. A entrada de dados deve continuar
até que o usuário informe o valor -1, indicando o encerramento dos registros. O valor -1 não deve ser armazenado na lista.
após a coleta de dados, o programa deve exibir:

* A quantidade total de avaliações registradas
* A maior idade informada
* A menor idade informada
* A média das idades
* A quantidade de alunos com idade acima da média
"""

I = int(input("informe a idade: "))

A = []
count1 = 0
count = 0
media = 0
maior = menor = I

while I != -1:

    count += 1
    A.append(I)
    media = I / count

    if I > media:
        count1 += 1

    if I > maior:
        maior = I
    else:
        menor = I

    I = int(input("informe a idade: "))
print("Quantidade de alunos com idades acima da média:", count1)
print("Quantidade total de avaliações registradas:", count)
print("A maior idade informada:", maior)
print("A menor idade informada" ,menor)
print("A média das idades:" ,media)
