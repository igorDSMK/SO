from FIFO import *
from Otimo import *
from LRU import *

######################

entradas = "entrada.txt"
paginas = []
quadros = 0
entrada = open(entradas, "r")
quadros = int(entrada.readline())

for line in entrada:
    paginas.append(line)
    
for i in range(0, len(paginas)):
    paginas[i] = int(paginas[i]) 

fifo (quadros, paginas)
otimos (quadros, paginas)
lru (quadros, paginas)
