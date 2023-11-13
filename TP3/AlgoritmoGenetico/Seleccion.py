# from Cromosoma import Cromosoma
import random
import numpy as np
# import math
# Clase estatica

class Seleccion:

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