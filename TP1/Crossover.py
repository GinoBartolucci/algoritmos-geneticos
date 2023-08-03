# from Cromosoma import Cromosoma
# import random

# class Crossover:

#     @staticmethod    
#     def corte(cromosoma1:Cromosoma,cromosoma2:Cromosoma) -> list:
        
#         if random.random() < Cromosoma.getProbCrossover():
#             punto_corte = random.randint(0,len(cromosoma1.genes))
#             hijo1 = Cromosoma(cromosoma1.genes[:punto_corte] + cromosoma2.genes[punto_corte:])
#             hijo2 = Cromosoma(cromosoma2.genes[:punto_corte] + cromosoma1.genes[punto_corte:])
#             return True,hijo1,hijo2
#         else:
#             return False,cromosoma1,cromosoma2

# from Cromosoma import Cromosoma
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
        