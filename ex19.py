#Temos um site de venda, queremos filtrar nossos usuários para receberem os anúncios corretos, conforme a tabela
#Menor de 15 anos: Oferecer artigos infantis
#Entre 15 e 21 feminino: Oferecer maquiagem e moda
#Entre 15 e 32 e atleta masculino: Oferecer artigos exportivos
#Entre 15 e 21 não atleta masculino: Oferecer videogames
#Entre 21 e 32 masculino não atleta: Oferecer livros, jardinagem e eletrodomesticos
#Entre 22 e 35 feminino: Oferecer artigos esportivos e itens de casa

idade = int(input("insira sua idade"))
genero = input("insira seu genero")
profissao = input("insira sua profissao")

if idade <= 15:
    print("Oferecer artigos infantis")
elif idade >= 15 and idade <= 21 and genero == "feminino":
    print("Oferecer maquiagem e moda")
elif idade >= 15 and idade <= 32 and profissao == "atleta":
    print("Oferecer artigos exportivos")
elif idade >= 15 and idade <= 21 and profissao != "atleta":
    print("Oferecer videogames")
elif idade >= 21 and idade <= 32 and profissao != "atleta":
    print("Oferecer livros, jardinagem e eletrodomesticos")
elif idade >= 22 and idade <= 35 and genero == "feminino":
    print("Oferecer artigos esportivos e itens de casa")

