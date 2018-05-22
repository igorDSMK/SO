def lru(quadros, paginas):
    mem = []
    contador = 0
        
    for element in paginas:        
        itBusca = element
        if itBusca not in mem:
            contador += 1
            if len(mem) == quadros:
                mem.pop(0)
                mem.append(itBusca)                
            else:
                mem.append(itBusca)
        else:
            mem.remove(itBusca)
            mem.append(itBusca)
            
    print("LRU", contador)
