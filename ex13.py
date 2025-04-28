#cadastro de alunos em uma escola. Escreva um programa que solicite ao usúario o nome, idade e turma de um aluno, armazene as informações em variáveis, exiba uma mensagem como: "aluno cadastrado com o sucesso: [Nome], [Idade], anos, turma [Turma], verifique se a idade é maior ou igual a 6 anos para validar a matricula."

nome = input("insira o nome do aluno")
idade = int(input("insira a idade do aluno"))
turma = input("insira a turma do aluno")

if idade >= 6:
    print("aluno cadastrado com o sucesso: {nome}, {idade}, anos, turma {turma}.")
else:
    print("acesso invalido.")