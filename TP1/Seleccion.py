# from Cromosoma import Cromosoma
import random

# Clase estatica

class Seleccion:
    @staticmethod
    def ruleta(cromosomas:list,vueltas=1):
        def generar_ruleta(cromosomas):
            ruleta = []
            tamanio_ruleta = len(cromosomas)
            for cromosoma in cromosomas:
                espacios_a_ocupar = int(round(cromosoma.fitness,1) * tamanio_ruleta)
                for iteracion in range(espacios_a_ocupar):
                    ruleta.append(cromosoma)
            return ruleta
        
        def girar_ruleta(ruleta,vueltas):
            if vueltas == 1:
                return random.choice(ruleta)
            elif vueltas > 1: 
                return list(map(lambda iteracion: random.choice(ruleta), range(vueltas)))
        
        ruleta = generar_ruleta(cromosomas)
        return girar_ruleta(ruleta,vueltas=vueltas)
 
 
    @staticmethod
    def torneo(cromosomas:list):
        pass

    @staticmethod
    def elitismo(cromosomas:list):
        pass
