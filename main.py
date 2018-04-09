#main
def Sort(ar):    
    menor = 0
    x = 0
    r = len(ar)
    for i in range(0, r-1):
        menor = i
        for j in range(i+1, r):
            if ar[j][0] < ar[menor][0]:
                menor = j
        if i !=menor:
            temp = ar[menor]
            ar[menor] = ar[i]
            ar[i] = temp
    return

def Sort2(ar):    
    menor = 0
    x = 0
    r = len(ar)
    for i in range(0, r-1):
        menor = i
        for j in range(i+1, r):
            if ar[j][1] < ar[menor][1]:
                menor = j
        if i !=menor:
            temp = ar[menor]
            ar[menor] = ar[i]
            ar[i] = temp
    return

def FCFS():
    r = len(processos)
    esperaIsolada = 0
    esperas = [0]
    esperaTotal = 0
    for i in range(1, r): # media espera
        esperaIsolada += processos[i-1][1] - (processos[i][0] - processos[i-1][0])        
        esperas.append(esperaIsolada)
        esperaTotal += esperaIsolada
    mediaEspera = esperaTotal/r
    
    respostaIsolada = 0
    respostaTotal = 0
    for i in range(1, r): # media resposta
        respostaIsolada += processos[i-1][1] - (processos[i][0] - processos[i-1][0])
        respostaTotal += respostaIsolada
    mediaResposta = respostaTotal/r

    retornoIsolado = 0
    retornoTotal = 0    
    for i in range(0, r): #media retorno
        retornoIsolado = esperas[i] + processos[i][1]        
        retornoTotal += retornoIsolado        
    mediaRetorno = retornoTotal/r

    print("FCFS " + str(mediaRetorno) + " " + str(mediaResposta)
          + " " + str(mediaEspera))
    return

def SJF():
    r = len(processos)
    troca = 1
    aux = []
    for i in range(0, r):
        aux.append([0, 0])
        aux[i][0] = processos[i][0]
        aux[i][1] = processos[i][1]
    for i in range(0, r-1):
        if aux[i][0] == aux[i+1][0]:
            if aux[i][1] > aux[i+1][1]:
                temp = aux[i+1]
                aux[i+1] = aux[i]
                aux[i] = temp
    fila = []
    ordem = []
    tempo = aux[0][1]
    ordem.append([aux[0][0], aux[0][1]])
    del aux[0]
    remover = []
    while (aux):
        for i in range(0, len(aux)):
            if(aux[i][0] <= tempo):                            
                fila.append([aux[i][0], aux[i][1]])
                remover.append([aux[i][0], aux[i][1]])                
        for i in range(0, len(remover)):            
            aux.remove(remover[0])
            del remover[0]
        if (fila):
            Sort2(fila)
            ordem.append([fila[0][0], fila[0][1]])
            tempo += fila[0][1]
            del fila[0]
        else:
            tempo += 1    
    while(fila):
        for i in range(0,len(fila)):
            Sort2(fila)
            ordem.append([fila[0][0], fila[0][1]])
            tempo += fila[0][1]
            del fila[0]
    print(ordem)
    return

############################

entradas = input()
entradas += ".txt"
processos = []
entrada = open(entradas,"r")    
for line in entrada:
    processos.append(line.split(" "))
entrada.close()
x = 0
for element in processos:
    processos[x][0] = int(processos[x][0])
    processos[x][1] = int(processos[x][1])
    x = x + 1
    
Sort(processos)
#FCFS()
SJF()
