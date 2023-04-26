
from DNA import DNA
from Graficador import *
from Seleccion import Seleccion







def ciclo(poblacion,fObjetivo,fFitness,numero_ciclo):
    DNA1 =  DNA(poblacion)
    res_objetivo = DNA1.calcular_objetivo(fObjetivo)
    res_fitness = DNA1.calcular_fitness(fFitness)
    
    encabezado = ['Poblacion(10)', 'Valor objetivo', 'Valor fitness']
    
    filas = []
    poblacion_info,info_decimal,info_fitness,info_objetivo = DNA1.get_info_poblacion()

    fila_suma = ["Suma", res_objetivo["Suma"], res_fitness["Suma"]]
    fila_promedio = ["Promedio", res_objetivo["Promedio"], res_fitness["Promedio"]]
    fila_maximo = ["Maximo", res_objetivo["Maximo"], res_fitness["Maximo"]]

    
    filas.extend(poblacion_info)
    filas.extend([fila_suma,fila_promedio,fila_maximo]) 

    # numero_ciclo = str(numero_ciclo) if numero_ciclo > 9 else f'0{numero_ciclo}'

    crearTabla(encabezado, filas) 
    graph_to_png(f'Tabla_I{numero_ciclo}')

    crearPieChart(encabezado,info_decimal)
    graph_to_png(f'Torta-I{numero_ciclo}')
    crearGraficoFuncion(funcion=funcion_objetivo,dominio=[0,2**30-1],puntos=[info_decimal,info_objetivo])
    graph_to_png(f'Grafico-I{numero_ciclo}')

    nueva_poblacion = Seleccion.ruleta(poblacion,vueltas=10)
    # porcentaje_ocupado = list(map(lambda x: x/len(nueva_poblacion), [nueva_poblacion.count(cromosoma) for cromosoma in poblacion]))
    # crearPieChart(poblacion, porcentaje_ocupado)
    # graph_to_png(f'TortaRuleta-I{numero_ciclo}')


    return nueva_poblacion



if __name__ == '__meain__':
    
 
    # poblacion = generar_poblacion(10, 30)
    poblacion = DNA.generar_poblacion(10, 30)
    funcion_objetivo = lambda x: (x /( (2**30) -1 ))**2
    fitness = lambda obj,sum_obj: obj/sum_obj
   

    
    DNA1 = DNA(poblacion)
    res_objetivo = DNA1.calcular_objetivo(funcion_objetivo)
    res_fitness = DNA1.calcular_fitness(fitness)

    print(res_objetivo)
    print(res_fitness)


    encabezado = ['Poblacion(10)', 'Valor objetivo', 'Valor fitness']
    
    filas = []
    poblacion_info,info_decimal,info_fitness,info_objetivo = DNA1.get_info_poblacion()

    fila_suma = ["Suma", res_objetivo["Suma"], res_fitness["Suma"]]
    fila_promedio = ["Promedio", res_objetivo["Promedio"], res_fitness["Promedio"]]
    fila_maximo = ["Maximo", res_objetivo["Maximo"], res_fitness["Maximo"]]

    
    filas.extend(poblacion_info)
    filas.extend([fila_suma,fila_promedio,fila_maximo])

    # poblacion_decimal = [cromosoma.decimal for cromosoma in poblacion]
    # objetivos_calculado = [cromosoma.objetivo for cromosoma in poblacion]
    # fitness_calculado = [cromosoma.fitness for cromosoma in poblacion]


    crearTabla(encabezado, filas) 
    graph_to_png('Tabla_I0')

    crearPieChart(encabezado,info_decimal)
    graph_to_png('Torta-I0')
    crearGraficoFuncion(funcion=funcion_objetivo,dominio=[0,2**30-1],puntos=[info_decimal,info_objetivo])
    graph_to_png('Grafico-I0')

    poblacion_selccionada = Seleccion.ruleta(poblacion,vueltas=10)

    for i in range(1,len(poblacion_selccionada),2):
        cromosoma_1 = poblacion_selccionada[i-1]
        cromosoma_2 = poblacion_selccionada[i]
        hijo1,hijo2 = cromosoma_1.crossover(cromosoma_2)
        poblacion_selccionada[i-1] = hijo1
        poblacion_selccionada[i] = hijo2

    print(poblacion_selccionada)

    # porcentaje_ocupado = list(map(lambda x: x/len(poblacion_selccionada), [poblacion_selccionada.count(cromosoma) for cromosoma in poblacion]))
    # crearPieChart(poblacion, porcentaje_ocupado)
    # graph_to_png('TortaRuleta-I0')

    # elementos_elegidos = girar_ruleta(ruleta, 10)
    # nueva_poblacion = crear_poblacionNueva(elementos_elegidos)
    

if __name__ == '__main__':
    ciclos = 10
    funcion_objetivo = lambda x: (x /( (2**30) -1 ))**2
    fitness = lambda obj,sum_obj: obj/sum_obj
    # poblaciones = []

    poblacion = DNA.generar_poblacion(10, 30)
    # poblaciones.append(poblacion)


    for i in range(ciclos):
        nueva_poblacion = ciclo(poblacion,funcion_objetivo,fitness,i)
        poblacion = nueva_poblacion
        # poblaciones.append(poblacion)    
        print('---------------------')
        