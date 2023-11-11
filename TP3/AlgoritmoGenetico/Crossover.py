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
            return [-1] * len(cromosoma1.genes),[-1] * len(cromosoma2.genes)
        def copiar_genes(cromosoma,genes_hijo):
            for i in range(len(cromosoma.genes)):
                if cromosoma.genes[i] == cromosoma.genes[punto_inicio]:
                    genes_hijo[i] = cromosoma.genes[i]
            return genes_hijo
        
        punto_inicio =  random.randint(0, len(cromosoma1.genes) - 1)
        genes_hijo1, genes_hijo2 = inicializar_genes_hijos(cromosoma1,cromosoma2)
        while True:
            genes_hijo1 = copiar_genes(cromosoma1,genes_hijo1)
            genes_hijo2 = copiar_genes(cromosoma2,genes_hijo2)
            
            # Encontrar el siguiente punto de inicio
            punto_inicio = -1
            for i in range(len(genes_hijo1)):
                if genes_hijo1[i] == -1:
                    punto_inicio = i
                    break
            # Si se han copiado todos los genes, terminar el crossover
            if punto_inicio == -1:
                break
 
 
        return True, genes_hijo1, genes_hijo2
        