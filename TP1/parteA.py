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
poblacion_binarios = f.convertirPoblacionBin(poblacion_decimal)

#Marco de datos inicial
marcoDeDatos = f.generarDataFrame(poblacion_decimal, poblacion_binarios, COEF)
marcoDeDatos_stats = f.generarEstadisticas(marcoDeDatos)
print('CICLO: 0')
print('\n TABLA DE DATOS: \n',marcoDeDatos)
print('\n ESTADISTICAS: \n',marcoDeDatos_stats)
for i in range(0, CICLOS):
    # Seleccion
    seleccion = f.ruleta(marcoDeDatos, CANTIDAD_POBLACION)
    #print('\nRULETA: ')
    #print('\n'.join(map(str, seleccion)))
    # Crossover
    crossover = f.crossover(seleccion, PROB_CROSSOVER)
    #print('\nCROSSOVER: ')
    #print('\n'.join(map(str, crossover)))
    # Mutacion
    mutantes = f.mutacion(crossover, PROB_MUTACION)
    #falta mutacion
    # nueva poblacion
    #print('-------------------------------------------------------------------------')
    #print('\nCICLO: ', i+1)
    marcoDeDatos = f.generarDataFrame(f.convertirPoblacionDecimal(mutantes), mutantes, COEF)
    marcoDeDatos_stats = f.generarEstadisticas(marcoDeDatos)
    #print('\n TABLA DE DATOS: \n',marcoDeDatos)
    #print('\n ESTADISTICAS: \n',marcoDeDatos_stats)

print('\n TABLA DE DATOS: \n',marcoDeDatos)
print('\n ESTADISTICAS: \n',marcoDeDatos_stats)
    

