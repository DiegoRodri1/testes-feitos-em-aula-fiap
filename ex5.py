#5

nome = input("Digite o nome do vendedor: ")

quantidade = int(input("Quantidade de produtos vendidos: "))

valor_total = float(input("Valor total das vendas (R$): "))

salario_base = 1800.00
comissao_fixa = 150.00 * quantidade
comissao_percentual = 0.03 * valor_total

salario_final = salario_base + comissao_fixa + comissao_percentual

print("Vendedor!!")
print("Seu salario saira por: ", salario_final)

