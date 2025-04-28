#Verificação de Maiores de Idade. Desenvolva um programa que: Solicite o ano de nascimento de uma pessoa. Exiba uma mensagem informando se ela é maior de idade (>= 18 anos) ou não.

ano_nascimento = int(input("insira o ano de nascimento"))
idade = 2025 - ano_nascimento

if idade >= 18:
    print("maior de idade")
else:   
    print("menor de idade")