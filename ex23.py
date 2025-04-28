# Tabuada com VetoresPeça ao usuário para digitar um número inteiro. Crie uma lista chamada tabuada que contenha os resultados da tabuada desse número (1 a 10). Use o laço for para preencher a lista com os resultados e depois exiba os valores armazenados.

num = int(input("insira um numero"))
tabuada = [num * i for i in range(1, 11)]
print(tabuada)