#Jogo de Adivinhação com Vetores Crie um programa onde o computador sorteia um número entre 1 e 20.Armazene os palpites do usuário em uma lista chamada palpites. Use um laço while para permitir que o usuário continue tentando até acertar. Ao final, exiba todos os palpites que o usuário forneceu.

import random

num = random.randint(1, 20)
palpites = []

while True:
    palpite = int(input("insira um numero"))
    palpites.append(palpite)
    if palpite == num:
        print("acertou")
        break
