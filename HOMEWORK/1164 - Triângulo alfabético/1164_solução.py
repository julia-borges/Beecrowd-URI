numero = int(input())

alfabeto = ('A','B','C' ,'D','E', 'F','G','H','I', 'J', 'K', 'L','M','N','O','P','Q', 'R', 'S','T', 'U', 'V','W', 'X','Y','Z')
s = 0
for letra in alfabeto:
    if s < numero:
        s += 1
        print(letra*s)