#Multiplicação de Elementos da Lista Crie uma lista chamada valores com 4 números inteiros fornecidos pelo usuário.Peça ao usuário um número adicional e multiplique cada elemento da lista pelo número fornecido, usando um laço for.Exiba os novos valores da lista.

valores = []

for i in range(4):
    num = int(input("insira um numero"))
    valores.append(num)

num_adicional = int(input("insira um numero"))

for i in range(len(valores)):
    valores[i] *= num_adicional

print(valores)