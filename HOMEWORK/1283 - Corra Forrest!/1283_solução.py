v = int(input())
a = 0
c = 0
lista = []

while v >=0:
    a += v
    c += 1
    lista.append(v)
    v = int(input())
    media = a/c

print(f"MEDIA: {media:.2f}") 

# MEDIA: 501.67
#lista: [161, 563, 781]

for i in range(len(lista)):
    if lista[i] < media:
        print(lista[i])
        i+=1