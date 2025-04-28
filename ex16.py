#Cálculo de Média de Notas. Faça um programa que: Peça ao usuário três notas. Calcule a média aritmética das notas. Informe se o aluno está aprovado (Média >= 7), em recuperação (média entre 5 e 7) ou reprovado (média < 5).

nota1 = float(input("insira a primeira nota"))
nota2 = float(input("insira a segunda nota"))
nota3 = float(input("insira a terceira nota"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7: 
    print("aprovado")
elif media >= 5 and media < 7:
    print("recuperacao")
else: 
    print("reprovado")