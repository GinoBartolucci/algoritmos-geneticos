import random
from Crossover import Crossover

class Cromosoma:

    prob_crossover = 0.75
    prob_mut = 0.05

    @staticmethod
    def setProbCrossover(probabilidad_crossover):
        probabilidad_crossover = probabilidad_crossover

    @staticmethod
    def setProbMutacion(probabilidad_mutacion):
        probabilidad_mutacion = probabilidad_mutacion
    
    @staticmethod
    def getProbCrossover():
        return Cromosoma.prob_crossover
    
    @staticmethod
    def getProbMutacion():
        return Cromosoma.prob_mut

   
    def __init__(self,genes,fitness=None) -> None:
        self.genes = genes
        self.decimal = self.genesToDecimal()
        self.fitness = fitness 
        self.objetivo = None
        self.hijos = []

    def genesToDecimal(self):
        "Transforma la lista de genes (numero binario) a decimal"
        cadena = ""
        for gen in self.genes:
            cadena += str(gen) 
        return int(cadena,2)
    
    def __str__(self) -> str:
        "Devuelve el valor del cromosoma"
        return str(self.decimal)
    


        # return ''.join(str(gen) for gen in self.genes)

    def __list__(self) -> list:
        "Devuelve el valor del cromosoma"
        return [self.decimal,self.fitness,self.objetivo]
    
    # def __dict__(self) -> dict:


    # def __int__(self):
    #     return int(self.__str__(), 2)
    # def addChildrens(self,*childrens):
    #     "Agrega los hijos al cromosoma"
    #     self.hijos.extend(childrens)

    def createChildern(self,genes):
        "Crea los hijos a partir de los genes"
        self.hijos.append(Cromosoma(genes))

    def crossover(self,otro_cromosoma):
        "Realiza el crossover entre dos cromosomas"
        seRealizoCrossOver,genes_hijo1,genes__hijo2= Crossover.corte(self,otro_cromosoma)
        hijo1 = Cromosoma(genes_hijo1).mutar()
        hijo2 = Cromosoma(genes__hijo2).mutar()
        # hijo1.mutar()
        # hijo2.mutar()

        # pueede ser completamente inservible
        # if seRealizoCrossOver:
            # self.addChildrens(hijo1,hijo2)
        return hijo1,hijo2
        
    def mutar(self):
        "Mutacion de un gen aleatorio"
        if random.random() < Cromosoma.getProbMutacion():
            posicion_random = random.int(0,len(self.genes))
            self.genes[posicion_random] = not self.genes[posicion_random]


