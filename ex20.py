#Verificação de acesso ao clube. Crie um programa em Python que determine se uma pessoa pode entrar em um clube com as seguites condições: Precisa ter mais de 18 anos. Se não for membro, deve pagar um ingresso. Se estiver acompanhado por um membro, paga meia entrada.

idade = int(input("insira sua idade"))
membro = input("voce e um membro?")
acompanhado = input("voce esta acompanhado?")

if idade >= 18:
    if membro == "sim":
        print("bem vindo")
    else:
        if acompanhado == "sim":
            print("pagar meia entrada")
        else:
            print("pagar ingresso")
            if acompanhado == "nao":
                print("pagar ingresso") 

 