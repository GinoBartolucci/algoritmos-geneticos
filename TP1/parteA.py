import numpy as np
import funciones as f

PROB_CROSSOVER = 0.75
PROB_MUTACION = 0.05
CICLOS = 200
CANTIDAD_POBLACION = 10
COEF = 1073741823 # 2^30-1


rng = np.random.default_rng() # Random Number Generator
# El 12345 es la semilla, poner sin semilla para q en cada ejecución genere nuevos aleatorios.

#Poblacion inicial
poblacion_decimal = rng.integers(low=0, high=COEF, size=CANTIDAD_POBLACION)
poblacion_binarios = f.Funciones.convertirPoblacionBin(poblacion_decimal)

#Marco de datos inicial
marcoDeDatos = f.Funciones.generarDataFrame(poblacion_decimal, poblacion_binarios, COEF)
marcoDeDatos_stats = f.Funciones.generarEstadisticas(marcoDeDatos)
print('CICLO: 0')
print('\n TABLA DE DATOS: \n',marcoDeDatos)
print('\n ESTADISTICAS: \n',marcoDeDatos_stats)
for i in range(0, CICLOS):
    # Seleccion
    seleccion = f.Funciones.ruleta(marcoDeDatos, CANTIDAD_POBLACION)
    #print('\nRULETA: ')
    #print('\n'.join(map(str, seleccion)))
    # Crossover
    crossover = f.Funciones.crossover(seleccion, PROB_CROSSOVER)
    #print('\nCROSSOVER: ')
    #print('\n'.join(map(str, crossover)))
    # Mutacion
    mutantes = f.Funciones.mutacion(crossover, PROB_MUTACION)
    #falta mutacion
    # nueva poblacion
    #print('-------------------------------------------------------------------------')
    #print('\nCICLO: ', i+1)
    marcoDeDatos = f.Funciones.generarDataFrame(f.Funciones.convertirPoblacionDecimal(mutantes), mutantes, COEF)
    marcoDeDatos_stats = f.Funciones.generarEstadisticas(marcoDeDatos)
    #print('\n TABLA DE DATOS: \n',marcoDeDatos)
    #print('\n ESTADISTICAS: \n',marcoDeDatos_stats)

print('\n TABLA DE DATOS: \n',marcoDeDatos)
print('\n ESTADISTICAS: \n',marcoDeDatos_stats)
    

