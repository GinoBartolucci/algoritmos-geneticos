import random 
# from Seleccion import Seleccion
from Cromosoma import Cromosoma


class DNA: 

    @staticmethod
    def generar_poblacion(cantidad_cromosomas:int, cantidad_genes:int):
        """
            -> list:Cromosoma
            cantidad_cromomas: int
            cantidad_genes: int
        """
        poblacion = []
        for iteracion in range(cantidad_cromosomas):
            cromosoma = DNA.generar_cromosoma(cantidad_genes)
            poblacion.append(cromosoma)
        return poblacion
 


    @staticmethod
    def generar_poblacion_numeros(cantidad_cromosomas:int):
        """
            -> list:Cromosoma
            cantidad_cromomas: int
        """
        poblacion = []
        for iteracion in range(cantidad_cromosomas):
            genes = random.sample(range(0, 23), 23)
            cromosoma = Cromosoma(genes=genes)
            poblacion.append(cromosoma)
        return poblacion
    

    def __init__(self,poblacion:list=None,ciclos:int=20):
        self.poblacion = poblacion
        self.ciclos = ciclos 
 
    def calcular_objetivo(self,funcion):
        for cromosoma in self.poblacion:
            distancia_total = 0
            distancia_total += funcion(cromosoma.genes[-1],cromosoma.genes[0])
            
            for posicion in range(0,len(cromosoma.genes)-1):
                ciudad_A,ciudad_B = cromosoma.genes[posicion],cromosoma.genes[posicion+1]
                distancia_ciudades = funcion(ciudad_A,ciudad_B) 
                distancia_total += distancia_ciudades
            index = self.poblacion.index(cromosoma)
            
            self.poblacion[index].objetivo = distancia_total
 
        objetivos = []
        for cromosoma in self.poblacion:
            objetivos.append(cromosoma.objetivo)


        return objetivos

    def calcular_fitness(self,funcion):
        for cromosoma in self.poblacion:
            fitness = funcion(cromosoma.objetivo)
            cromosoma.fitness = fitness 
 


    @staticmethod
    def cruzar_poblacion_numeros(poblacion):
        """
            -> list:Cromosoma
        """
        hijos = []
        # Seleccionamos los cromosomas a cruzar
        for posicion in range(0,len(poblacion),2):
            cromosoma_1 = poblacion[posicion]
            cromosoma_2 = poblacion[posicion+1]
            # Cruzamos los cromosomas
            hijo1,hijo2 = cromosoma_1.cruzar_ciclico(cromosoma_2)
            hijos.append(hijo1)
            hijos.append(hijo2)
    
        return hijos
