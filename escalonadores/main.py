from fcfs import *
from sjf import *
from rr import *


############################

entradas = "entrada1.txt"
processos = []
entrada = open(entradas,"r")    
for line in entrada:
    processos.append(line.split(" "))
entrada.close()

for i in range(0, len(processos)):
    processos[i][0] = int(processos[i][0])
    processos[i][1] = int(processos[i][1])

    
processos = sorted(processos, key=lambda proc: proc[0])

FCFS(processos)
SJF(processos)
RR(processos, 2)
