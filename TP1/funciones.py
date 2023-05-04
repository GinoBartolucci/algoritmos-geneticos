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

def funcionObjetivo(poblacion_binaria, coeficiente):
    poblacion = convertirPoblacion(poblacion_binaria, False)
    funObjetivo = []
    # El nombre cromosoma es por semántica, en realidad va a trabajar con cada valor decimal
    for cromosoma in poblacion:
        funObjetivo.append((int(cromosoma)/int(coeficiente))**2)
    # convertir lista en numpy arrray (para operaciones matemáticas))
    return funObjetivo    

def funcionFitness(poblacion_binaria, coeficiente):
    fitness = []
    funObjetivo = funcionObjetivo(poblacion_binaria, coeficiente)
    # El nombre cromosoma es por semántica, en realidad va a trabajar con cada valor decimal
    for objetivo in funObjetivo:
        fitness.append((objetivo/sum(funObjetivo)))
    # convertir lista en numpy arrray (para operaciones matemáticas)
    return fitness

def generarDataFrame(pob_bin, coeficiente):
    pob_dec = convertirPoblacion(pob_bin, False)
    data = {'Decimales': pob_dec, 'Binarios': pob_bin, 
            'FuncionObjetivo':np.array(funcionObjetivo(pob_bin,coeficiente))}
    dataFrame = pd.DataFrame(data)
    dataFrame['Fitness'] = np.array(funcionFitness(pob_bin, coeficiente))
    return dataFrame

def generarEstadisticas(dataFrame):
    stats = {'Suma':[ dataFrame['FuncionObjetivo'].sum(), dataFrame['Fitness'].sum() ], 
              'Promedio': [ dataFrame['FuncionObjetivo'].mean(), dataFrame['Fitness'].mean() ], 
              'Maximo': [ dataFrame['FuncionObjetivo'].max(), dataFrame['Fitness'].max() ]}
    dataFrame_stats = pd.DataFrame(stats, index = ['Función objetivo', 'Fitness'])
    return dataFrame_stats

def ruleta(pob_bin, coeficiente):  # pasar marco de datos
    # Asigna probabilidad basada en el fitness
    cantidad_poblacion = len(pob_bin)
    cromosomas = np.array(pob_bin)
    probabilidades = np.array(funcionFitness(pob_bin, coeficiente))
    np.random.seed()
    salida = np.random.choice(cromosomas, size=int(cantidad_poblacion), p=probabilidades)
    salida = salida.tolist()
    return salida

def torneo(poblacion_binaria, coeficiente):
    salida = []
    fitness = np.array(funcionFitness(poblacion_binaria, coeficiente))
    cantidad_poblacion = len(poblacion_binaria)
    poblacion_binaria = np.array(poblacion_binaria)
    for i in range(0, cantidad_poblacion):
        posiblesCantidades = [x for x in range(1, (cantidad_poblacion+1))]
        np.random.seed()
        cantidadMiembrosTorneo = np.random.choice(
            posiblesCantidades, size=1)
        # Trabaja directamente con los fitness de los cromósomas
        miembrosTorneo = np.random.choice(fitness, size=cantidadMiembrosTorneo[0], replace=False)
        ganador = np.amax(miembrosTorneo)
        indiceGanador = np.where(fitness == ganador)  # retorna ndarray
        cromosomaGanador = poblacion_binaria[indiceGanador[0][0]]
        salida.append(cromosomaGanador)
    return salida

def elitismo(poblacion_binaria, cantidad, coeficiente):
    fitness = []
    fitness = funcionFitness(poblacion_binaria, coeficiente)
    elites = []
    for i in range(0, cantidad):
        # busca cual es cromosoma con mayor fitness
        ganador = max(fitness)
        indiceGanador = fitness.index(ganador)
        cromosomaGanador = poblacion_binaria[indiceGanador]
        # agrega el cromosoma a la lista de elites y lo elimina de la lista de cromosomas para buscar el siguiente
        elites.append(cromosomaGanador)
        fitness.remove(ganador)
        poblacion_binaria.remove(cromosomaGanador)
    return [elites, poblacion_binaria]

def crossover(padres_binarios, prob_corssover):  # Pasar ndarray cromosomas padres
    hijos = []
    cantidad_poblacion = len(padres_binarios)
    genes = len(padres_binarios[0])
    padres_binarios = np.array(padres_binarios)
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
            primerTiraGenesPadre1 = padres_binarios[i][0:posicionCorte]
            segundaTiraGenesPadre1 = padres_binarios[i][posicionCorte:genes]
            primerTiraGenesPadre2 = padres_binarios[i+1][0:posicionCorte]
            segundaTiraGenesPadre2 = padres_binarios[i+1][posicionCorte:genes]
            hijos.append(primerTiraGenesPadre1 + segundaTiraGenesPadre2)  # Hijo 1
            hijos.append(primerTiraGenesPadre2 + segundaTiraGenesPadre1)  # Hijo 2
        else:
            hijos.append(padres_binarios[i])
            hijos.append(padres_binarios[i+1])
    return hijos

