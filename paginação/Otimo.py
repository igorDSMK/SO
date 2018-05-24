def highest (ar):
    maior = ar[0]
    maiorend = 0
    for i in range (1, len(ar)):
        if maior < ar[i]:
            maior = ar[i]
            maiorend = i
    return maiorend


def otimos (quadros, mem):
    paginas = []
    contador = 0
    posicoes = []

    for i in range (0, quadros):
        posicoes.append(0)

    for i in range(0, len(mem)):        
        itBusca = mem[i]
        if itBusca not in paginas:
            contador += 1
            if len(paginas) == quadros:
                for j in range(0, len(paginas)):
                    posicoes[j] = 0
                    elem = paginas[j]
                    for k in range(i+1, len(mem)):
                        posicoes[j] += 1                        
                        if elem == mem[k]:                            
                            break
                paginas.pop(highest(posicoes))
                paginas.append(itBusca)                
            else:
                paginas.append(itBusca)            
                
    print ("OTM", contador)
