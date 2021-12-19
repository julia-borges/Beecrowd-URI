divida = int(input())
mensalidade = int(input())
c = 0

while divida > 0:
    if divida >= mensalidade:
        c += 1
        print(f"pagamento: {c}")
        print(f"antes = {divida}")
        divida = divida - mensalidade
        print(f"depois = {divida}")
        print("-"*5)
    else:
        c += 1
        print(f"pagamento: {c}")
        print(f"antes = {divida}")
        divida = divida - mensalidade
        print(f"depois = 0")
        print("-"*5)