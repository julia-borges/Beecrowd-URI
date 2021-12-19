def exibe(tabela):
    for c in range(qtd):
        if sinal[c]:
            print(f"*({(c+1):03}) original: {(resultado[c][0]):05.2f} | final: {(resultado[c][1]):05.2f}")
        else:
           print(f"-({(c+1):03}) original: {(resultado[c][0]):05.2f} | final: {(resultado[c][1]):05.2f}")

qtd = int(input())
nota = []
atividade = []

for i in range(qtd):
    nota.append(float(input()))
for i in range(qtd):
    atividade.append(float(input()))

sinal = []
resultado = []
alterado = 0

for i in range(qtd):
    if atividade[i] == 10:
        bonus = nota[i] + 2.00
        if bonus <= 10:
            resultado.append([nota[i], bonus])
            alterado += 1
            sinal.append(True)
            
        elif bonus == 12:
            resultado.append([nota[i], 10.00])
            sinal.append(False)
        else:
            resultado.append([nota[i], 10.00])
            alterado+=1
            sinal.append(True)
    else:
        resultado.append([nota[i], nota[i]])
        sinal.append(False)

print(f'NOTAS ALTERADAS: {alterado}')
exibe(resultado)