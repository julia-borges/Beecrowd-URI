entrada = int(input())  
impar = (entrada % 2)!= 0 
par = (entrada % 2) == 0  

if impar == True:
    primeiro_number_impar = entrada - 2
    segundo_number_par = primeiro_number_impar + 3
else:
    primeiro_number_impar = entrada - 1
    segundo_number_par = primeiro_number_impar + 3

print(f"{primeiro_number_impar} {segundo_number_par}")