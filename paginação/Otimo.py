def lowest (ar):
    maior = ar[0]
    maiorend = 0
    for i in range (1, len(ar)):
        if maior < ar[i]:
            maior = ar[i]
            maiorend = i
    return maiorend


def otimos (quadros, paginas):
    mem = []
    contador = 0
    posicoes = []

    for i in range (0, quadros):
        posicoes.append(0)

    for i in range(0, len(paginas)):        
        itBusca = paginas[i]
        if itBusca not in mem:
            contador += 1
            if len(mem) == quadros:
                for j in range(0, len(mem)):
                    posicoes[j] = 0
                    elem = mem[j]
                    for k in range(i+1, len(paginas)):
                        posicoes[j] += 1                        
                        if elem == paginas[k]:                            
                            break
                mem.pop(lowest(posicoes))
                mem.append(itBusca)                
            else:
                mem.append(itBusca)                
                
    print ("OTM", contador)
