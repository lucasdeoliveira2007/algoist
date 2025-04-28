# Filtrando Números Pares e Ímpares Crie uma lista chamada numeros com 8 números inteiros escolhidos pelo usuário. Use um laço for para dividir os números em duas listas: pares e impares.

numeros = []

for i in range(8):
    num = int(input("insira um numero"))
    numeros.append(num)

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Numeros:", numeros)
print("Pares:", pares)
print("Impares:", impares)