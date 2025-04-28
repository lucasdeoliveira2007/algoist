#crie um programa que peça o valor da compra e use if para calcular o desconto baseado em faixas de preço (exemplo: compras acima de R$ 1000,00 ganham 10% de desconto).
vl_cm = int(input("insira o valor da compra"))
if vl_cm ==200 or vl_cm <=100:
    desconto = vl_cm * 0.02
    print("deconto de 20%")
elif vl_cm ==500 or 700:
    desconto = vl_cm * 0.04
    print("deconto é de 30%")
else:
    desconto= 0
    print("não foi inserido nnhum valor")
    
                    
