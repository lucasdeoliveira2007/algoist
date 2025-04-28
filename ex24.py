# Encontrando o Maior e o Menor Número Crie uma lista chamada numeros com 5 números inteiros fornecidos pelo usuário. Use um laço for para determinar e exibir o maior e o menor número da lista.

numeros = []

for i in range(5):
    num = int(input("insira um numero"))
    numeros.append(num)

maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"o maior numero e {maior} e o menor numero e {menor}")
