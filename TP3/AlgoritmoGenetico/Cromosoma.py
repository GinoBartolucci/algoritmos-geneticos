import random
import numpy as np
from Crossover import Crossover

class Cromosoma:

    prob_crossover = 0.75 
    prob_mut = 0.05

    @staticmethod
    def setProbCrossover(probabilidad_crossover):
        Cromosoma.prob_crossover = probabilidad_crossover

    @staticmethod
    def setProbMutacion(probabilidad_mutacion):
        Cromosoma.prob_mut = probabilidad_mutacion
    
    @staticmethod
    def getProbCrossover():
        return Cromosoma.prob_crossover
    
    @staticmethod
    def getProbMutacion():
        return Cromosoma.prob_mut
    

   
    def __init__(self,genes,fitness=None) -> None:
        self.genes = genes
        # self.decimal = self.genesToDecimal()
        self.fitness = fitness 
        self.objetivo = None
        self.hijos = []
        # self.decimalToBinary()
 
 

 
    
    def __str__(self) -> str:
        "Devuelve el valor del cromosoma"
        return str(f"{self.genes} {self.objetivo}")
 

    def __list__(self) -> list:
        "Devuelve el valor del cromosoma"
        return [self.fitness,self.objetivo]
 
 
    def createChildern(self,genes):
        "Crea los hijos a partir de los genes"
        self.hijos.append(Cromosoma(genes))

 
    def cruzar_ciclico(self,otro_cromosoma):
        "Realiza el crossover ciclico entre dos cromosomas"
        seRealizoCrossOver,genes_hijo1,genes__hijo2= Crossover.ciclico(self,otro_cromosoma)
        hijo1 = Cromosoma(genes_hijo1)
        hijo2 = Cromosoma(genes__hijo2) 
        
        # hijo1.mutar() # falta ver como mutar
        # hijo2.mutar() # falta ver como mutar (convertirlo a binario, mutar y volver a decimal?)

        return hijo1,hijo2

    def mutar(self):
        genes = len(self.genes)
        opciones = [True, False]
        np.random.seed()
        prob_mut = np.array([Cromosoma.getProbMutacion(), (1-Cromosoma.getProbMutacion())])
        debeMutar = np.random.choice(opciones, size=1, p=prob_mut)[0]
        if debeMutar:
            posiciones = [x for x in range(0, genes)]
            probMutacion = [1/genes for x in range(0, genes)]
            posicionMutacion_1 = np.random.choice(posiciones, size=1, p=probMutacion)[0]
            posicionMutacion_2 = np.random.choice(posiciones, size=1, p=probMutacion)[0]
            ciudad_1 = self.genes[posicionMutacion_1]
            ciudad_2 = self.genes[posicionMutacion_2]

            self.genes[posicionMutacion_1] = ciudad_2
            self.genes[posicionMutacion_2] = ciudad_1


    