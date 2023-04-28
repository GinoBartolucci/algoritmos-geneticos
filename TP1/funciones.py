import numpy as np
import pandas as pd

class Funciones:
    @classmethod
    def generarDataFrame(cls, pob_dec, pob_bin, coeficiente):
        data = {'Decimales': pob_dec, 'Binarios': pob_bin, 
                'FuncionObjetivo':Funciones.funcionObjetivo(pob_dec,coeficiente)}
        dataFrame = pd.DataFrame(data)
        dataFrame['Fitness'] = dataFrame['FuncionObjetivo'] / dataFrame['FuncionObjetivo'].sum()
        return dataFrame

    @classmethod
    def generarEstadisticas(cls, dataFrame):
        stats = {'Suma':[ dataFrame['FuncionObjetivo'].sum(), dataFrame['Fitness'].sum() ], 
                 'Promedio': [ dataFrame['FuncionObjetivo'].mean(), dataFrame['Fitness'].mean() ], 
                 'Maximo': [ dataFrame['FuncionObjetivo'].max(), dataFrame['Fitness'].max() ]}
        dataFrame_stats = pd.DataFrame(stats, index = ['Función objetivo', 'Fitness'])
        return dataFrame_stats

    @classmethod
    def funcionObjetivo(cls, poblacion_decimal, coeficiente):
        colObjetivo = []
        # El nombre cromosoma es por semántica, en realidad va a trabajar con cada valor decimal
        for cromosoma in poblacion_decimal:
            colObjetivo.append((int(cromosoma)/int(coeficiente))**2)
        # convertir lista en numpy arrray (para operaciones matemáticas)
        npColObjetivo = np.array(colObjetivo)
        return npColObjetivo

    @classmethod
    def ruleta(cls, dataFrame, cantidad_poblacion):  # pasar marco de datos
        # Asigna probabilidad basada en el fitness
        probabilidades = np.array(dataFrame['Fitness'])
        cromosomas = np.array(dataFrame['Binarios'])
        np.random.seed()
        salida = np.random.choice(cromosomas, size=int(cantidad_poblacion), p=probabilidades)
        return salida

    @classmethod
    def torneo(cls, dataFrame):
        salida = []
        fitness = np.array(dataFrame['Fitness'])
        cromosomas = np.array(dataFrame['Binarios'])
        for i in range(0, 10):
            posiblesCantidades = [x for x in range(1, 11)]
            np.random.seed()
            cantidadMiembrosTorneo = np.random.choice(
                posiblesCantidades, size=1)
            # Trabaja directamente con los fitness de los cromósomas
            miembrosTorneo = np.random.choice(fitness, size=cantidadMiembrosTorneo[0], replace=False)
            ganador = np.amax(miembrosTorneo)
            indiceGanador = np.where(fitness == ganador)  # retorna ndarray
            cromosomaGanador = cromosomas[indiceGanador[0][0]]
            salida.append(cromosomaGanador)
        return salida

    @classmethod
    def elitismo(cls, dataFrame, cantidad=2):
        fitness = np.array(dataFrame['Fitness'])
        cromosomas = np.array(dataFrame['Binarios'])
        elites = []
        for i in range(0, cantidad):
            # busca cual es cromosoma con mayor fitness
            ganador = np.amax(fitness)
            indiceGanador = np.where(fitness == ganador)
            cromosomaGanador = cromosomas[indiceGanador[0][0]]
            # agrega el cromosoma a la lista de elites y lo elimina de la lista de cromosomas para buscar el siguiente
            elites.append(cromosomaGanador)
            fitness = np.delete(fitness, indiceGanador[0][0])
            cromosomas = np.delete(cromosomas, indiceGanador[0][0])
        return elites

    @classmethod
    def crossover(cls, padres_bianrio, prob_corssover):  # Pasar ndarray cromosomas padres
        hijos = []
        for i in range(0, 10, 2):
            opciones = [True, False]
            np.random.seed()
            # Probabilidades de cada opción
            prob_cross = np.array([prob_corssover, (1-prob_corssover)])
            cross = np.random.choice(opciones, size=1, p=prob_cross)
            if cross[0]:
                posiciones = [x for x in range(0, 30)]
                probCorte = [1/30 for x in range(0, 30)]
                # Devuelve ndarray de 1 elemento
                corte = np.random.choice(posiciones, size=1, p=probCorte)
                posicionCorte = corte[0]
                primerTiraGenesPadre1 = padres_bianrio[i][0:posicionCorte]
                segundaTiraGenesPadre1 = padres_bianrio[i][posicionCorte:30]
                primerTiraGenesPadre2 = padres_bianrio[i+1][0:posicionCorte]
                segundaTiraGenesPadre2 = padres_bianrio[i+1][posicionCorte:30]
                hijos.append(primerTiraGenesPadre1 + segundaTiraGenesPadre2)  # Hijo 1
                hijos.append(primerTiraGenesPadre2 + segundaTiraGenesPadre1)  # Hijo 2
            else:
                hijos.append(padres_bianrio[i])
                hijos.append(padres_bianrio[i+1])
        return hijos
    
    @classmethod
    def convertirPoblacionBin(cls, pob_dec):
        pob_bin = []
        for decimal in pob_dec:
            # convirtiendo cada número decimal en binario de 8 dígitos.
            pob_bin.append(format(decimal,'030b'))
        return pob_bin
    
    @classmethod
    def convertirPoblacionDecimal(cls, pob_bin):
        pob_dec = []
        for binario in pob_bin:
            # convirtiendo cada número binario en decimal.
            pob_dec.append(int(binario,2))
        return pob_dec
    
    @classmethod
    def mutacion(cls, hijos_bin, prob_mutacion):
        hijos_mutados = []
        for hijo in hijos_bin:
            opciones = [True, False]
            np.random.seed()
            # Probabilidades de cada opción
            prob_mut = np.array([prob_mutacion, (1-prob_mutacion)])
            mut = np.random.choice(opciones, size=1, p=prob_mut)
            if mut[0]:
                posiciones = [x for x in range(0, 30)]
                probMutacion = [1/30 for x in range(0, 30)]
                # Devuelve ndarray de 1 elemento
                posicionMutacion = np.random.choice(posiciones, size=1, p=probMutacion)
                posicionMutacion = posicionMutacion[0]
                if hijo[posicionMutacion] == '0':
                    hijo = hijo[:posicionMutacion] + '1' + hijo[posicionMutacion+1:]
                else:
                    hijo = hijo[:posicionMutacion] + '0' + hijo[posicionMutacion+1:]
            hijos_mutados.append(hijo)
        return hijos_mutados