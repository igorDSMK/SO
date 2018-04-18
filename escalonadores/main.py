from fcfs import *
from sjf import *
from rr import *


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

Sort(processos)

FCFS(processos)
SJF(processos)
RR(processos, 2)
