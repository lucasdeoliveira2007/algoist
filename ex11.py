#faça um algoritimo que realize o cadastro de uma pssoa, a senha deve ter no minimo 8 caracters. O e-mail cadastrado deve estar todo minusculo, depois solicite um login com os dados recem cadstrados.
email_certo = input("crie um email")
email_certo = str_lower (email_certo)

senha = input("crie uma senha")
if len(senha) < 8:
    print("senha muito curta")
else:
    senha_certa = senha 
    email = input("insira um email")
    senha = input("insira uma senha")
    if email == email_certo:
        if senha == senha_certa:
            print("bem vindo")
        else:
            print("email ou senha incorreta")