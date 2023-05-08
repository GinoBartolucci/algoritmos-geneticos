import numpy as np
import pandas as pd

def convertirPoblacion(pob_ini, bin=True): # Pasar False para convertir a decimal
    pob_fin = []
    for numero in pob_ini:
        if bin:
            # convirtiendo cada número decimal en binario de 8 dígitos.
            pob_fin.append(format(numero,'030b'))
        else:
            pob_fin.append(int(str(numero), 2))
    return pob_fin

def mutacion(hijos_binarios, prob_mutacion):
        hijos_mutados = []
        genes = len(str(hijos_binarios[0]))
        for hijo in hijos_binarios:
            opciones = [True, False]
            np.random.seed()
            # Probabilidades de cada opción
            prob_mut = np.array([prob_mutacion, (1-prob_mutacion)])
            mut = np.random.choice(opciones, size=1, p=prob_mut)
            if mut[0]:
                posiciones = [x for x in range(0, genes)]
                probMutacion = [1/genes for x in range(0, genes)]
                # Devuelve ndarray de 1 elemento
                posicionMutacion = np.random.choice(posiciones, size=1, p=probMutacion)
                posicionMutacion = posicionMutacion[0]
                if hijo[posicionMutacion] == '0':
                    hijo = hijo[:posicionMutacion] + '1' + hijo[posicionMutacion+1:]
                else:
                    hijo = hijo[:posicionMutacion] + '0' + hijo[posicionMutacion+1:]
            hijos_mutados.append(hijo)
        return hijos_mutados

def funcionObjetivo(poblacion_binarios, coeficiente):
    poblacion = convertirPoblacion(poblacion_binarios, False)
    fun_objetivo = []
    for cromosoma in poblacion:
        fun_objetivo.append((int(cromosoma)/int(coeficiente))**2)
    # convertir lista en numpy arrray (para operaciones matemáticas))
    return fun_objetivo    

def funcionFitness(poblacion_binarios, coeficiente):
    fitness = []
    fun_objetivo = funcionObjetivo(poblacion_binarios, coeficiente)
    for objetivo in fun_objetivo:
        fitness.append((objetivo/sum(fun_objetivo)))
    # convertir lista en numpy arrray (para operaciones matemáticas)
    return fitness

def generarDataFrame(pob_bin, coeficiente):
    pob_dec = convertirPoblacion(pob_bin, False)
    data = {'Decimales': pob_dec, 'Binarios': pob_bin, 
            'FuncionObjetivo':np.array(funcionObjetivo(pob_bin,coeficiente))}
    data_frame = pd.DataFrame(data)
    data_frame['Fitness'] = np.array(funcionFitness(pob_bin, coeficiente))
    return data_frame

def generarEstadisticas(data_frame):
    stats = {'Suma':[ data_frame['FuncionObjetivo'].sum(), data_frame['Fitness'].sum() ], 
              'Promedio': [ data_frame['FuncionObjetivo'].mean(), data_frame['Fitness'].mean() ], 
              'Maximo': [ data_frame['FuncionObjetivo'].max(), data_frame['Fitness'].max() ]}
    data_frame_stats = pd.DataFrame(stats, index = ['Función objetivo', 'Fitness'])
    return data_frame_stats

def ruleta(pob_bin, coeficiente):
    # Asigna probabilidad basada en el fitness
    cantidad_poblacion = len(pob_bin)
    cromosomas = np.array(pob_bin)
    probabilidades = np.array(funcionFitness(pob_bin, coeficiente))
    np.random.seed()
    binarios_ruleta = np.random.choice(cromosomas, size=int(cantidad_poblacion), p=probabilidades)
    binarios_ruleta = binarios_ruleta.tolist()
    return binarios_ruleta

def torneo(poblacion_binarios, coeficiente):
    binarios_torneo = []
    fitness = np.array(funcionFitness(poblacion_binarios, coeficiente))
    cantidad_poblacion = len(poblacion_binarios)
    poblacion_binarios = np.array(poblacion_binarios)
    for i in range(0, cantidad_poblacion):
        posiblesCantidades = [x for x in range(1, (cantidad_poblacion+1))]
        np.random.seed()
        cantidadMiembrosTorneo = np.random.choice(posiblesCantidades, size=1)
        # Trabaja directamente con los fitness de los cromósomas
        miembrosTorneo = np.random.choice(fitness, size=cantidadMiembrosTorneo[0], replace=False)
        ganador = np.amax(miembrosTorneo)
        indiceGanador = np.where(fitness == ganador)  # retorna ndarray
        cromosomaGanador = poblacion_binarios[indiceGanador[0][0]]
        binarios_torneo.append(cromosomaGanador)
    return binarios_torneo

def elitismo(poblacion_binarios, cantidad, coeficiente):
    fitness = funcionFitness(poblacion_binarios, coeficiente)
    no_elites = poblacion_binarios
    elites = []
    for i in range(0, cantidad):
        # busca cual es cromosoma con mayor fitness
        ganador = max(fitness)
        indiceGanador = fitness.index(ganador)
        cromosomaGanador = no_elites[indiceGanador]
        # agrega el cromosoma a la lista de elites y lo elimina de la lista de cromosomas para buscar el siguiente
        elites.append(cromosomaGanador)
        fitness.remove(ganador)
        no_elites.remove(cromosomaGanador)
    return [elites, no_elites]

def crossover(poblacion_binarios, prob_corssover):
    hijos_crossover = []
    cantidad_poblacion = len(poblacion_binarios)
    genes = len(poblacion_binarios[0])
    poblacion_binarios = np.array(poblacion_binarios)
    for i in range(0, cantidad_poblacion, 2):
        opciones = [True, False]
        np.random.seed()
        # Probabilidades de cada opción
        prob_cross = np.array([prob_corssover, (1-prob_corssover)])
        cross = np.random.choice(opciones, size=1, p=prob_cross)
        if cross[0]:
            posiciones = [x for x in range(0, genes)]
            probCorte = [(1/genes) for x in range(0, genes)]
            # Devuelve ndarray de 1 elemento
            corte = np.random.choice(posiciones, size=1, p=probCorte)
            posicionCorte = corte[0]
            primerTiraGenesPadre1 = poblacion_binarios[i][0:posicionCorte]
            segundaTiraGenesPadre1 = poblacion_binarios[i][posicionCorte:genes]
            primerTiraGenesPadre2 = poblacion_binarios[i+1][0:posicionCorte]
            segundaTiraGenesPadre2 = poblacion_binarios[i+1][posicionCorte:genes]
            hijos_crossover.append(primerTiraGenesPadre1 + segundaTiraGenesPadre2)  # Hijo 1
            hijos_crossover.append(primerTiraGenesPadre2 + segundaTiraGenesPadre1)  # Hijo 2
        else:
            hijos_crossover.append(poblacion_binarios[i])
            hijos_crossover.append(poblacion_binarios[i+1])
    return hijos_crossover

