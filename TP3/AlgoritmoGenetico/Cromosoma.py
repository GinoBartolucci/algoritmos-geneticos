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
        self.fitness = fitness 
        self.objetivo = None
        self.hijos = []
        
    def __str__(self) -> str:
        "Devuelve el valor del cromosoma"
        return str(f"{self.genes} {self.objetivo}")
 

    def __list__(self) -> list:
        "Devuelve el valor del cromosoma"
        return [self.fitness,self.objetivo]


 
    def cruzar_ciclico(self,otro_cromosoma):
        "Realiza el crossover ciclico entre dos cromosomas"
        seRealizoCrossOver,genes_hijo1,genes__hijo2= Crossover.ciclico(self,otro_cromosoma)
        hijo1 = Cromosoma(genes_hijo1)
        hijo2 = Cromosoma(genes__hijo2) 
        hijo1.mutar()  
        hijo2.mutar()  

        return hijo1,hijo2

    def mutar(self):
        if random.random() < Cromosoma.getProbMutacion():
            i, j = random.sample(range(len(self.genes)-1), 2)
            self.genes[i], self.genes[j] = self.genes[j], self.genes[i]

    