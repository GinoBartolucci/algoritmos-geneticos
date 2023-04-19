probabilidad_crossover = 0.75
probabilidad_mutacion = 0.05
ciclos = 20

cromosomas = []

objetivos = []

def fitness(cromosoma):
    objetivo_cromosoma = objetivo(cromosoma)
    objetivos.push(objetivo_cromosoma)
    # Deberia ser una suma de todos los cromosomas en decimal
    suma_objetivos = sum(objetivos)
    return objetivo_cromosoma/suma_objetivos

def objetivo(cromosoma):
    coeficiente = 2**30 -1
    # Deberia pasar el cromosoma binario (x) a decimal
    return (cromosoma/coeficiente)**2
   

def generar_cromosomas():
    cromosoma = []
    #genrar 10 genes
    #def generar_genes():
        #for g in range(10):
