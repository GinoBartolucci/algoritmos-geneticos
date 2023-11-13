import random 
# from Seleccion import Seleccion
from Cromosoma import Cromosoma

# la clase poblacion, tendremos tantos DNA como ciclos
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
    def generar_cromosoma(cantidad_genes):
        genes = [] 
        for iteracion in range(cantidad_genes):
            gen = random.randint(0,1) 
            genes.append(gen) 
        return Cromosoma(genes=genes)

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
        self.fitness = {"Suma":0,"Promedio":0,"Maximo":0}
        self.objetivo = {"Suma":0,"Promedio":0,"Maximo":0}
        self.ciclos = ciclos 
 
    def calcular_objetivo(self,funcion):
        """
        Mi idea aca es ir sumando la distancia entre las distintas ciudades
        tener en cuenta que debo tomar entre dos ciudades la distancia
        """
        print("self.poblacion",len(self.poblacion))
        for cromosoma in self.poblacion:
            distancia_total = 0
            for posicion in range(0,len(cromosoma.genes)-2):
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
            # print(cromosoma.objetivo)
            fitness = funcion(cromosoma.objetivo)
            cromosoma.fitness = fitness 

        return self.fitness
 

    def get_info_poblacion(self):
        info = []
        info_decimal = []
        info_fitness = []
        info_objetivo = []

        for cromosoma in self.poblacion:
 
            info_fitness.append(cromosoma.fitness)
            info_objetivo.append(cromosoma.objetivo)

        return info,info_decimal,info_fitness,info_objetivo


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