inicio = int(input())
fim = (int(input())) + 1
qtd_bissexto = 0 #
 
for ano in range(inicio, fim): #2000
    if ano% 4 ==0 and ano%100 !=0:
        qtd_bissexto += 1
        print(ano)
    elif ano% 400 ==0:
        qtd_bissexto += 1
        print(ano)
            
print(f"bissextos: {qtd_bissexto}")