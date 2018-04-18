def RR(processos, quantum):
    
    tempo = 0
    aux = []
    ended = 0
    prontos = []    
    esperas = []
    respostas = []
    respostaSoma = 0
    retornoIndiv = 0
    ex = 0
    
    for i in range(0, len(processos)):
        aux.append([0, 0])
        esperas.append(0)
        aux[i][0] = processos[i][0]
        aux[i][1] = processos[i][1]

    for i in range (0, len(aux)):            
        if (aux[0][0] <= tempo):
            prontos.append(aux.pop(0))
            respostas.append([0, 0])
        else:
            break
                
    while(len(aux) or len(prontos)):
        
        if (prontos):
            ex = 1
            for i in range (0, quantum):
                ended = 0
                prontos[0][1] -= 1
                respostas[0][0] = 1
            
                for i in range (1, len(prontos)):
                    esperas[i] += 1

                for i in range (1, len(prontos)):
                    if respostas[i][0] == 0:
                        respostas[i][1] += 1

                if prontos[0][1] <= 0:
                    prontos.pop(0)
                    respostaSoma += respostas[0][1]
                    respostas.pop(0)
                    tempo += 1               
                    ended = 1
                    break
                tempo += 1
        else:
            tempo += 1

        for i in range (0, len(aux)):
            if (aux[0][0] <= tempo):
                prontos.append(aux.pop(0))
                respostas.append([0, 0])
            else:
                break
            
        if (prontos):                
            if ended == 0 and ex == 1:
                prontos.append(prontos.pop(0))
                respostas.append(respostas.pop(0))
        ex = 0

    for i in range (0, len(processos)):
        retornoIndiv += processos[i][1]
    retornoIndiv += sum(esperas)
    
    esperaMedia = sum(esperas)/len(processos)
    respostaMedia = respostaSoma/len(processos)
    retornoMedio = retornoIndiv/len(processos)
    print("RR " + str(retornoMedio) + " " + str(respostaMedia) + " " + str(esperaMedia))    
    return
