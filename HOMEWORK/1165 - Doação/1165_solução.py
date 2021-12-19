contadora = 0
soma  = 0
n= float(input())

while n != -1.0:
    soma += n
    contadora += 1
    n= float(input())
    
reais = soma * 2.50
    
print(f"VC$ {reais / 2.50:.2f}")
print(f"R$ {reais:.2f}")