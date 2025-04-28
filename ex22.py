#Contando Elementos em uma Lista Crie uma lista chamada palavras com 6 palavras fornecidas pelo usuário.Use um laço for para contar quantas palavras têm mais de 5 caracteres.Exiba o total no final.

palavras = []

for i in range(6):
    palavra = input("insira uma palavra")
    palavras.append(palavra)

total = 0

for palavra in palavras:
    if len(palavra) > 5:
        total += 1

print(f"total de palavras com mais de 5 caracteres: {total}")