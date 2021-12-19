carrinho = input().split()

for i in range(len(carrinho)):
    carrinho[i] = int(carrinho[i])

listacomando = list()
comando = input().split()

while comando[0] != 'encerrar':
    listacomando.append(comando)
    comando = input().split()
    
for comando in listacomando:
    
    if comando[0] == 'exibir':
        carrinho = sorted(carrinho)
        print(*carrinho)
    
    elif comando[0] == 'adicionar':
        carrinho.append(int(comando[1]))
  
    elif comando[0] == 'remover':
        quant = comando[1].split()
        quant = int(quant[0])
        if quant in carrinho:
            carrinho.remove(quant)
        else:
            print(f'código {quant} não encontrado')
if carrinho != []:
    carrinho = sorted(carrinho)
    print(*carrinho)