#Login Bancário. Crie um sistema de login simples: Soloicite ao usuário e a senha. Compare os valores inseridos com credenciais previamente armazenadas em variáveis (ex: usuario = "admin", senha = "1234"). Exiba mensagens de sucesso ou erro depedendo da entrada.

usuario = input("insira o nome do usuario")
senha = input("insira a senha")

if usuario == "admin" and senha == "1234":
    print("login efetuado com sucesso")
else:
    print("login efetuado incorreto")