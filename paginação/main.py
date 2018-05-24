from FIFO import *
from Otimo import *
from LRU import *

######################

entradas = "entrada.txt"
mem = []
quadros = 0
entrada = open(entradas, "r")
quadros = int(entrada.readline())

for line in entrada:
    mem.append(line)
    
for i in range(0, len(mem)):
    mem[i] = int(mem[i]) 

fifo (quadros, mem)
otimos (quadros, mem)
lru (quadros, mem)
