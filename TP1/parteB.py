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
    seleccion = f.torneo(poblacion_binarios, COEF)
    #print('\nTORNEO: ')
    #print('\n'.join(map(str, seleccion)))
    # Crossover
    crossover = f.crossover(seleccion, PROB_CROSSOVER)
    #print('\nCROSSOVER: ')
    #print('\n'.join(map(str, crossover)))
    # Mutacion
    poblacion_binarios = f.mutacion(crossover, PROB_MUTACION)
    #print('\nMUTACION: ')
    #print('\n'.join(map(str, mutantes)))
    if(i+1 == CICLOS):
        print('-------------------------------------------------------------------------\nCICLO: ', i+1)
        marcoDeDatos = f.generarDataFrame(poblacion_binarios, COEF)
        marcoDeDatos_stats = f.generarEstadisticas(marcoDeDatos)
    #print('\n TABLA DE DATOS: \n',marcoDeDatos)

print('\n TABLA DE DATOS: \n',marcoDeDatos)
print('\n ESTADISTICAS: \n',marcoDeDatos_stats)