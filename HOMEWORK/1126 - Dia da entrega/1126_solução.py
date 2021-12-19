dia = input()

if dia == 'domingo':
    dia_numero = 0
elif dia == 'segunda':
    dia_numero = 1
elif dia == 'terca':
    dia_numero = 2
elif dia == 'quarta':
    dia_numero = 3 
elif dia == 'quinta':
    dia_numero = 4
elif dia == 'sexta':
    dia_numero = 5
elif dia == 'sabado':
    dia_numero = 6

prazo = int(input())

if prazo == 0:
    print("chega hoje!")
else:
    entrega= dia_numero + prazo
    if entrega == 7:
        print("sera entregue domingo")
    elif entrega == 1 or entrega == 8:
        print("sera entregue segunda")
    elif entrega == 2 or entrega == 9:
        print("sera entregue terca")
    elif entrega == 3 or entrega == 10:
        print("sera entregue quarta")
    elif entrega == 4 or entrega == 11:
        print("sera entregue quinta")
    elif entrega == 5 or entrega == 12:
        print("sera entregue sexta")
    elif entrega == 6:
        print("sera entregue sabado")