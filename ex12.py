#um banco deseja diminuir a quantidade de contas sem saldo do seu sistema. Desenvolver um algoritimo que verifique o saldo da conta (solicite essa informação para o responsavel pela execuçaõ do processo) Se o saldo for 0 alterar status da conta para inteiro
status_conta = True

valor_saldo = int(input("digite seu saldono banco"))
if valor_saldo >=0.01:
    print("sua conta ainda esta ativa")
elif valor_saldo <0:
    print("negociar a divida")
else:
    status_conta = False
    print("conta inativa")