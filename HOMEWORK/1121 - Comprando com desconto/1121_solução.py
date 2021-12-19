valor = float(input())
qtd = int(input())

bruto = valor * qtd
desconto = (10 + qtd) / 100
valor_desc = bruto * desconto
valor_final = bruto - valor_desc

print(f"{bruto:.2f}")
print(f"{valor_final:.2f}")