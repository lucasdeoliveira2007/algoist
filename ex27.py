# Lista de NomesCrie uma lista chamada nomes e insira os nomes de 5 amigos.Use um laço for para exibir os nomes em ordem alfabética.

nomes = []

for i in range(5):
    nome = input("insira um nome")
    nomes.append(nome)

nomes.sort()

for nome in nomes:
    print(nome)
