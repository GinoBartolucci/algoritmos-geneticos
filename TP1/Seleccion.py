# from Cromosoma import Cromosoma
import random
import numpy as np
# import math
# Clase estatica

class Seleccion:
    @staticmethod
    def ruleta(cromosomas:list,vueltas=1):

        def generar_ruleta(cromosomas):
            ruleta = []
            tamanio_ruleta = len(cromosomas) 
            for cromosoma in cromosomas:
                # espacios_a_ocupar = int(round(cromosoma.fitness,1) * tamanio_ruleta * 1000)
                espacios_a_ocupar = int( (cromosoma.fitness* 1000) ) #* tamanio_ruleta)
                for iteracion in range(espacios_a_ocupar):
                    ruleta.append(cromosoma)
            return ruleta
        
        def girar_ruleta(ruleta,vueltas):
            if vueltas == 1:
                return random.choice(ruleta)
            elif vueltas > 1:                 
                np.random.seed()
                # posicion_ruleta_random = random.randrange(start=0, stop=len(ruleta),step=1)
                # print(posicion_ruleta_random)

                return list(map(lambda iteracion: ruleta[random.randrange(start=0, stop=len(ruleta),step=1)], range(vueltas)))
        
        ruleta = generar_ruleta(cromosomas)
        return girar_ruleta(ruleta,vueltas=vueltas)
    
 
    @staticmethod
    # def torneo():
    def torneo(cromosomas:list, cantidad_poblacion):
        """ Retorna una lista con los ganadores de los torneos, estos son 
            los mejores cromosomas de la poblacion

            cromosomas: list<Cromosoma>
            cantidad_poblacion: int
            return: list<Cromosoma>
        """
        ganadores = []
        # pob_binarios = np.array(poblacion_binarios)
        # fitness = np.array(funcionFitness(pob_binarios))
        for ronda in range(0, cantidad_poblacion):
            posiblesCantidades = [x for x in range(1, (cantidad_poblacion+1))]
            np.random.seed()
            cantidad_participantes = np.random.choice(posiblesCantidades, size=1)[0]
            particpantes = np.random.choice(cromosomas, size=cantidad_participantes, replace=False)
            
            ganador = Seleccion._buscar_ganador(particpantes)
            ganadores.append(ganador)
        
        return ganadores

    @staticmethod
    def elitismo(cromosomas:list,cantidad:int):
        """ Retorna una lista con los mejores cromosomas de la poblacion 
            cromosomas: list<Cromosoma>
            cantidad: int
            return: list<Cromosoma>
        """
        elites = [] 
        for ronda in range(0, cantidad): 
            ganador = Seleccion._buscar_ganador(cromosomas)
            elites.append(ganador)
            cromosomas.remove(ganador)

        return elites

    @staticmethod
    def _buscar_ganador(cromosomas):
            ganador = None
            for cromosoma in cromosomas:
                if ganador == None or cromosoma.fitness > ganador.fitness:
                    ganador = cromosoma
            return ganador