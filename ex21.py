#Crie uma lista chamada numeros com 10 números inteiros escolhidos pelo usuário.Use um laço for para imprimir cada número da lista.Calcule e exiba a soma de todos os números usando outro laço for.

numeros = []

for i in range(10):
    num = int(input("insira um numero"))
    numeros.append(num)

soma = 0

for num in numeros:
    soma += num

print("Numeros:", numeros)
print("Soma:", soma)