import random

class Crossover:

    @staticmethod    
    def corte(cromosoma1,cromosoma2) -> list:
        # print("Probabilidad de crossover")
        if random.random() < cromosoma1.getProbCrossover():
            # print("#### CROSSOVER ####")
            punto_corte = random.randint(0,len(cromosoma1.genes))
            hijo1 =  cromosoma1.genes[:punto_corte] + cromosoma2.genes[punto_corte:] 
            hijo2 =  cromosoma2.genes[:punto_corte] + cromosoma1.genes[punto_corte:] 
            # print("Genes hijo 1 e hijo2 \n%s" % hijo1)
            # print(hijo2)
            # print("#### END ####")

            return True,hijo1,hijo2
        else:
            return False,cromosoma1.genes,cromosoma2.genes
        
    

    def ciclico(cromosoma1, cromosoma2): 
        hijo1, hijo2 = cromosoma1.genes.copy(), cromosoma2.genes.copy()

        punto_inicio = random.randint(0, len(cromosoma1.genes) - 1)
        punto_actual = punto_inicio
        genes_visitados = set()   

        while True:
            # Intercambiar genes
            hijo1[punto_actual], hijo2[punto_actual] = hijo2[punto_actual], hijo1[punto_actual]
            genes_visitados.add(punto_actual)

            # Encontrar el próximo índice en el ciclo
            punto_actual = cromosoma1.genes.index(cromosoma2.genes[punto_actual])

            se_completo_ciclo = punto_actual == punto_inicio
            if se_completo_ciclo:
                break

        # Llenar los genes que no están en el ciclo directamente de los padres
        for ciudad in range(len(cromosoma1.genes)):
            if ciudad not in genes_visitados:
                hijo1[ciudad] = cromosoma1.genes[ciudad]
                hijo2[ciudad] = cromosoma2.genes[ciudad]

        return True, hijo1, hijo2