#Simulação de Compra no Mercado. Desenvolva um programa que: Solicite ao usuário o nome de um produto, a quantidade comprada e o preço unitário. Calcule e exiba o total da compra (ex: Total: R$ [valor calculado]). Aplique um desconto de 5% se o valor total for maior que R$ 100.

nome_do_produto = input("insira o nome do produto")
quantidade = int(input("insira a quantidade comprada"))
preço_unitario = float(input("insira o preco unitario"))

total = quantidade * preço_unitario

if total >= 100:
    desconto = 0.05
    valor_com_desconto = total * (1 - desconto)
    print(f"desconto aplicado: 5%")
    print(f"valor final da compra: {valor_com_desconto}")
else:
    print("sem desconto")
    print(f"valor final da compra: {total}")

