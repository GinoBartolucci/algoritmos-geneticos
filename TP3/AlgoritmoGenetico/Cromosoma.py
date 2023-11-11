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

    def decimalToBinary(self):
        "Transforma el numero decimal a binario"
        if self.decimal and len(self.genes) == 0:
            return bin(self.decimal)[2:]
    
    def getGenesInStr(self):
        "Devuelve la lista de genes como string"
        return ''.join(str(gen) for gen in self.genes)
        # return self.genes

    def genesToDecimal(self):
        "Transforma la lista de genes (numero binario) a decimal"
        cadena = ""
        for gen in self.genes:
            cadena += str(gen) 
        return int(cadena,2)
    
    def __str__(self) -> str:
        "Devuelve el valor del cromosoma"
        return str(self.decimal)
 

    def __list__(self) -> list:
        "Devuelve el valor del cromosoma"
        return [self.fitness,self.objetivo]
 
 
    def createChildern(self,genes):
        "Crea los hijos a partir de los genes"
        self.hijos.append(Cromosoma(genes))

    def cruzar(self,otro_cromosoma):
        "Realiza el crossover entre dos cromosomas"
        seRealizoCrossOver,genes_hijo1,genes__hijo2= Crossover.corte(self,otro_cromosoma)
        hijo1 = Cromosoma(genes_hijo1)
        hijo2 = Cromosoma(genes__hijo2) 
        hijo1.mutar()
        hijo2.mutar()


        return hijo1,hijo2

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
            posicionMutacion = np.random.choice(posiciones, size=1, p=probMutacion)[0]
            self.genes[posicionMutacion] = int(not self.genes[posicionMutacion])
