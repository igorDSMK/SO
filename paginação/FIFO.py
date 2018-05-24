def fifo(quadros, mem):
    paginas = []
    contador = 0
        
    for element in mem:
        itBusca = element
        if itBusca not in paginas:
            contador += 1
            if len(paginas) == quadros:
                paginas.pop(0)
                paginas.append(itBusca)                
            else:
                paginas.append(itBusca)            

    print("FIFO", contador)
