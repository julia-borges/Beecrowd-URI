def linha():
    print('-'*10)

a = int(input())
b = int(input())

if a > b:
    print("Nenhuma tabuada no intervalo!")
else:
    while a <= b:
        i = 1
        while i <= 10:
            print(f"{a} x {i} = {a*i}")
            i += 1
        linha()
        a+=1