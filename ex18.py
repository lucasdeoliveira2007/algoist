#Calculo de Salario com Horas Extras. Crie um programa que:Peça o salario base, o numero de horas extras trabalhadas e o valor pago por hora extra. Calcule o valor total do salario (base + horas extras). Exiba o valor total do salario.

salario_base = int(input("insira o salario base"))
horas_extras = int(input("insira o numero de horas extras trabalhadas"))
valor_hora_extra = int(input("insira o valor pago por hora extra"))

salario_total = salario_base + (horas_extras * valor_hora_extra)

print(f"o salario total e {salario_total}")
