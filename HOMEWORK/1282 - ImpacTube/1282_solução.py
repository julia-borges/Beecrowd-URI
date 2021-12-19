def exibe(tabela):
    for registro in tabela:
        print(f'{registro[0]}: R$ {registro[1]:.2f}')

qtd = int(input())
canais = []

for i in range(qtd):
    canal = input().split(';')
    canal[1] = int(canal[1])
    canal[2] = float(canal[2])
    if canal[3] == 'sim':
        canal[3] = True
    else:
        canal[3] = False
    canais.append(canal)
    
x = float(input())
y = float(input())

bonus = []

for canal in canais:
    if canal[1] >= 1000:
        if canal[3]:
            calculo = (canal[1] // 1000) * x  + canal[2]
        else:
            calculo = (canal[1] // 1000) * y + canal[2]
        bonus.append([canal[0], calculo])
    else:
        bonus.append([canal[0], canal[2]])
  
print('-'*5)
print('BÔNUS')
print('-'*5)
exibe(bonus)