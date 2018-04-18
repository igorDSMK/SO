def FCFS(processos):
    tempo = 0
    esperas = 0
    respostas = 0
    retornos = processos[0][1]
    
    for i in range(1, len(processos)):
        if processos[i-1][1] - processos[i][0] + processos[i-1][0] <= 0:
            retornos += processos[i][1]            
        else:
            tempo += processos[i-1][1] - processos[i][0] + processos[i-1][0]
            esperas += tempo
            respostas += tempo
            retornos += tempo + processos[i][1]
            
    mediaEspera = esperas/len(processos)
    mediaResposta = respostas/len(processos)
    mediaRetorno = retornos/len(processos)

    print("FCFS " + str(mediaRetorno) + " " + str(mediaResposta)
          + " " + str(mediaEspera))
    return
