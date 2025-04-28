#Encontrando Palíndromos Crie uma lista chamada palavras com 5 palavras fornecidas pelo usuário. Use um laço for para verificar quais palavras são palíndromos (ou seja, que podem ser lidas da mesma forma de trás para frente, como "arara").Exiba as palavras palíndromas no final.

palavras = []

for i in range(5):
    palavra = input("insira uma palavra")
    palavras.append(palavra)

palindromos = []

for palavra in palavras:
    if palavra == palavra[::-1]:
        palindromos.append(palavra)

print("Palavras palindromas:", palindromos)