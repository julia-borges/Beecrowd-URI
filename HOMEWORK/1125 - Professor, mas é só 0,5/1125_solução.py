T = float(input())
P = float(input())
media= (T + P)/2

if media >=6:
    print("aprovado")#não passou
elif P >=0 <6: #passou aqui
    prova_sub = 4.60
    usar_prova_sub = (T + prova_sub)/2 #4,6
    if usar_prova_sub >=4.60:
        print("talvez com a sub")
    else:
        print("reprovado")