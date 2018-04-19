def SJF(processos):
    aux = []
    prontos = []
    tempo = 0
    esperas = 0
    respostas = 0
    
    for i in range(0, len(processos)):
        aux.append ([0, 0])
        aux[i][0] = processos[i][0]
        aux[i][1] = processos[i][1]

    for i in range (0, len(aux)):            
        if (aux[0][0] <= tempo):
            prontos.append(aux.pop(0))            
        else:
            break
    
    prontos = sorted(prontos, key=lambda proc: proc[1])
    
    while (len(aux) or len(prontos)):

        if(prontos):            
            tempo += prontos[0][1]
            
            for i in range (0, len(aux)):
                if (aux[0][0] <= tempo):
                    prontos.append(aux.pop(0))            
                else:
                    break
            
            for i in range (1, len(prontos)):
                respostas += prontos[0][1] - prontos[i][0] + prontos[0][0]
                esperas += prontos[0][1] - prontos[i][0] + prontos[0][0]
                prontos[i][0] = prontos[0][1]
            
            prontos.pop(0)
            
        else:
            tempo += 1
            
            for i in range (0, len(aux)):
                if (aux[0][0] <= tempo):
                    prontos.append(aux.pop(0))            
                else:
                    break
                
        prontos = sorted(prontos, key=lambda proc: proc[1])

    retornos = esperas
    for i in range (0, len(processos)):
        retornos += processos[i][1]
    

    retornoMedio = retornos/len(processos)        
    respostaMedia = respostas/len(processos)
    esperaMedia = esperas/len(processos)
    retornoMedio = round(retornoMedio, 1)        
    respostaMedia = round(respostaMedia, 1)
    esperaMedia = round(esperaMedia, 1)
    print("SJF " + str(retornoMedio) + " " + str(respostaMedia) + " " + str(esperaMedia))
    return
