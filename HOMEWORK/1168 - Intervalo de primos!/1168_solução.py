inicio = int(input())
fim = int(input())
qtd_primos = 0

def e_primo(valor):
    if valor < 2:
        return False # não é primo
    elif valor == 2:
        print(valor)
        return True # é primo
    else:
        for i in range(2,valor):
            if valor % i == 0:
                return False
        print(valor)
        return True        
                
if (inicio <= fim <= 5000):
    for i in range(inicio, fim + 1):
        if e_primo(i):
            qtd_primos +=1
            
    print(f"primos: {qtd_primos}")