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


    

    def __init__(self,poblacion:list=None,ciclos:int=20):
        self.poblacion = poblacion
        self.fitness = {"Suma":0,"Promedio":0,"Maximo":0}
        self.objetivo = {"Suma":0,"Promedio":0,"Maximo":0}
        self.ciclos = ciclos 
 
    def calcular_objetivo(self,funcion):
        
        for cromosoma in self.poblacion:
            objetivo = funcion(int(cromosoma.decimal))
            cromosoma.objetivo = objetivo
        
        self.objetivo["Suma"]  = sum([cromosoma.objetivo for cromosoma in self.poblacion])
        self.objetivo["Promedio"] = self.objetivo["Suma"]/len(self.poblacion)
        self.objetivo["Maximo"] = max([cromosoma.objetivo for cromosoma in self.poblacion])

        return self.objetivo

    def calcular_fitness(self,funcion):
        for cromosoma in self.poblacion:
            fitness = funcion(cromosoma.objetivo,self.objetivo["Suma"])
            cromosoma.fitness = fitness

        self.fitness["Suma"] = sum([cromosoma.fitness for cromosoma in self.poblacion])
        self.fitness["Promedio"] = self.fitness["Suma"]/len(self.poblacion)
        self.fitness["Maximo"] = max([cromosoma.fitness for cromosoma in self.poblacion])

        return self.fitness
 

    def get_info_poblacion(self):
        info = []
        info_decimal = []
        info_fitness = []
        info_objetivo = []

        for cromosoma in self.poblacion:
            cromosoma_info = cromosoma.__list__()
            
            info.append(cromosoma.getGenesInStr())
            info_decimal.append(cromosoma.decimal)
            info_fitness.append(cromosoma.fitness)
            info_objetivo.append(cromosoma.objetivo)

        return info,info_decimal,info_fitness,info_objetivo
    
    
    def cruzar_poblacion(self):
        """
            -> list:Cromosoma
        """
        hijos = []
        # Seleccionamos los cromosomas a cruzar
        for posicion in range(0,len(self.poblacion),2):
            cromosoma_1 = self.poblacion[posicion]
            cromosoma_2 = self.poblacion[posicion+1]
            # Cruzamos los cromosomas
            hijo1,hijo2 = cromosoma_1.cruzar(cromosoma_2)
            hijos.append(hijo1)
            hijos.append(hijo2)
    
        return hijos
    
            # Retornamos los cromosomas cruzados

        # Cruzamos los cromosomas
        # cromosomas_cruzados = self.cruzar(cromosomas_seleccionados)
        # Retornamos los cromosomas cruzados
        # return cromosomas_cruzados

    # def get_info_poblacion(self):
    #     """
    #     {
    #         "decimal": {
    #             "objetivo": 0.1244,
    #             "fitness": 0.1244
    #             "binario": 31232131,

    #             }

    #         }
    #     }
    #     """
    #     info = {}
    #     for cromosoma in self.poblacion:
    #         info[cromosoma.decimal] = {
    #             "objetivo": cromosoma.objetivo,
    #             "fitness": cromosoma.fitness,
    #             "binario": cromosoma.genes
    #         }
    #         # info.append(cromosoma.__list__())
    #     return info
    
        
    # def func_Objetivo(self, cromosoma):
    #     coeficiente = 2**30 -1
    #     return (cromosoma/coeficiente)**2
    
    # def func_Fitness(self, cromosomas):
    #     objetivos = []
    #     for cromosoma in cromosomas:
    #         objetivo = self.func_Objetivo(cromosoma)
    #         objetivos.append(objetivo)
    #     suma_objetivos = sum(objetivos)
    #     objetivos_calculado = list(map(lambda x: x/suma_objetivos, objetivos))
        
    #     return objetivos_calculado

    

