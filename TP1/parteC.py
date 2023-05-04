import numpy as np
import funciones as f

PROB_CROSSOVER = 0.75
PROB_MUTACION = 0.05
CICLOS = 200
CANTIDAD_POBLACION = 10
COEF = 1073741823 # (2^30)-1

rng = np.random.default_rng() # Random Number Generator

#Poblacion inicial
poblacion_decimal = rng.integers(low=0, high=COEF, size=CANTIDAD_POBLACION)
poblacion_binarios = f.convertirPoblacion(poblacion_decimal)

#Marco de datos inicial
marcoDeDatos = f.generarDataFrame(poblacion_binarios, COEF)
marcoDeDatos_stats = f.generarEstadisticas(marcoDeDatos)
print('CICLO: 0')
print('\n TABLA DE DATOS: \n',marcoDeDatos)
print('\n ESTADISTICAS: \n',marcoDeDatos_stats)
for i in range(0, CICLOS):
    # Seleccion
    seleccion = f.ruleta(poblacion_binarios, COEF)
    # Elitismo
    #print('\nTORNEO: ')
    #print('\n'.join(map(str, seleccion)))
    elitismo = f.elitismo(seleccion,2, COEF)
    #print('\nELITISMO: ')
    #print('\n'.join(map(str, elitismo)))
    # Crossover
    crossover = f.crossover(elitismo[1], PROB_CROSSOVER)
    # Mutacion
    mutantes = f.mutacion(crossover, PROB_MUTACION)
    poblacion_binarios = elitismo[0] + mutantes
    if(i+1 == CICLOS):
        print('-------------------------------------------------------------------------\nCICLO: ', i+1)
        marcoDeDatos = f.generarDataFrame(poblacion_binarios, COEF)
        marcoDeDatos_stats = f.generarEstadisticas(marcoDeDatos)
    #print('\n TABLA DE DATOS: \n',marcoDeDatos)

print('\n TABLA DE DATOS: \n',marcoDeDatos)
print('\n ESTADISTICAS: \n',marcoDeDatos_stats)