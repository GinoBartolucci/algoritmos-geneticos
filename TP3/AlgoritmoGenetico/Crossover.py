import random

class Crossover:

    @staticmethod    
    def corte(cromosoma1,cromosoma2) -> list:
        # print("Probabilidad de crossover")
        if random.random() < cromosoma1.getProbCrossover():
            # print("#### CROSSOVER ####")
            punto_corte = random.randint(0,len(cromosoma1.genes))
            genes_hijo1 =  cromosoma1.genes[:punto_corte] + cromosoma2.genes[punto_corte:] 
            genes_hijo2 =  cromosoma2.genes[:punto_corte] + cromosoma1.genes[punto_corte:] 
            # print("Genes hijo 1 e hijo2 \n%s" % genes_hijo1)
            # print(genes_hijo2)
            # print("#### END ####")

            return True,genes_hijo1,genes_hijo2
        else:
            return False,cromosoma1.genes,cromosoma2.genes
        
    @staticmethod
    def ciclico(cromosoma1,cromosoma2) -> list:
        def inicializar_genes_hijos(cromosoma1,cromosoma2):
            return cromosoma1.genes.copy(), cromosoma2.genes.copy()
        
        def copiar_genes(cromosoma,genes_hijo):
            for i in range(len(cromosoma.genes)):
                if genes_hijo[i] == -1:
                    genes_hijo[i] = cromosoma.genes[i]
            return genes_hijo
        
        genes_hijo1, genes_hijo2 = inicializar_genes_hijos(cromosoma1,cromosoma2)
        while -1 in genes_hijo1 or -1 in genes_hijo2:
            punto_inicio = random.randint(0, len(cromosoma1.genes) - 1)
            punto_actual = punto_inicio
            while True:
                genes_hijo1[punto_actual], genes_hijo2[punto_actual] = genes_hijo2[punto_actual], genes_hijo1[punto_actual]
                punto_actual = cromosoma1.genes.index(cromosoma2.genes[punto_actual])
                if punto_actual == punto_inicio:
                    break
 
        return True, genes_hijo1, genes_hijo2
        