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
    binarios_torneo = f.torneo(poblacion_binarios, COEF)
    binarios_crossover = f.crossover(binarios_torneo, PROB_CROSSOVER)
    poblacion_binarios = f.mutacion(binarios_crossover, PROB_MUTACION)

print('-------------------------------------------------------------------------\nCICLO: ', CICLOS)
marcoDeDatos = f.generarDataFrame(poblacion_binarios, COEF)
marcoDeDatos_stats = f.generarEstadisticas(marcoDeDatos)
print('\n TABLA DE DATOS: \n',marcoDeDatos)
print('\n ESTADISTICAS: \n',marcoDeDatos_stats)