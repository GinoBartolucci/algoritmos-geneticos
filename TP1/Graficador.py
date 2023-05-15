import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import Image, display


def hacerGrafico(estadisticas, iteracion):
    estadisticas["Iteración"]=[x for x in range(1,iteracion+1)]
    plt.figure(figsize=(20,20))
    plt.plot(estadisticas["Iteración"], estadisticas["Máximo"], 'b.-', label="Máximo")
    plt.plot(estadisticas["Iteración"], estadisticas["Mínimo"], 'r.-', label="Mínimo")
    plt.plot(estadisticas["Iteración"], estadisticas["Promedio"], 'g.-', label="Promedio")
    plt.legend()
    plt.title("Gráfica iteración: " + str(iteracion))
    plt.xticks(estadisticas["Iteración"][::1])
    plt.yticks(np.arange(0, 1.01, step=0.025))
    plt.xlabel("Iteraciones")
    plt.ylabel("F. Objetivo")
    plt.show()


def generarDataFrame(pob_dec, pob_bin,info_obj,info_fitness):
    data = {'Decimales': pob_dec, 'Binarios': pob_bin, 'FuncionObjetivo':info_obj,"fitness":info_fitness}
    dataFrame = pd.DataFrame(data)
    return dataFrame
    display(dataFrame)


def generarEstadisticas(dataFrame):
    stats = {'Suma':[ dataFrame['FuncionObjetivo'].sum(), dataFrame['Fitness'].sum() ], 'Promedio': [ dataFrame['FuncionObjetivo'].mean(), dataFrame['Fitness'].mean() ], 'Máximo': [ dataFrame['FuncionObjetivo'].max(), dataFrame['Fitness'].max() ], 'Mínimo': [ dataFrame['FuncionObjetivo'].min(), dataFrame['Fitness'].min() ]}
    dataFrame_stats = pd.DataFrame(stats, index = ['Función objetivo', 'Fitness'])
    return dataFrame_stats, stats
 

# left_coordinates=[1,2,3,4,5]
# heights=[10,20,30,15,40]
# bar_labels=['One','Two','Three','Four','Five']
# plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.6,color=['red','black'])
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title("A simple bar graph")
# plt.show()

def crearTabla(encabezado, filas):
    cantidad_filas = len(filas)
    cantidad_columnas = len(encabezado)
    # Creo la tabla
    tabla = plt.table(cellText=filas, colLabels=encabezado, loc='center')
    # Ajusto el tamaño de la tabla
    tabla.scale(1, 2)
    # Ajusto el tamaño de la figura
    plt.gcf().set_size_inches(18, 7)
    # Disminuyo la separacion entre celdas
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(16)

    # Saco los ejes
    plt.axis('off')
      
def crearGraficoFuncion(funcion,dominio,puntos):
    x = np.linspace(dominio[0], dominio[1])
    y = funcion(x)

    plt.plot(x, y)
    plt.gcf().set_size_inches(18, 7)
    plt.grid(True) 

    plt.plot(puntos[0],puntos[1], 'ro')    
    


def crearPieChart(encabezado, filas):
    """ 
        Crea un grafico de torta
            encabezado: lista de strings
            filas: lista de numeros
    """
    # Creo el grafico
    plt.pie(filas, labels=filas, autopct='%1.1f%%')
    # Ajusto el tamaño de la figura
    plt.gcf().set_size_inches(18, 7)
    # Lo muevo hacia la derecha 
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.8)
    # Muestro la leyenda
    plt.legend(encabezado, loc='center left', bbox_to_anchor=(1, 0.5))
    

def graph_to_png(nombre):
    try:
        plt.savefig(f'TP1/graficos/{nombre}.png')
    except FileNotFoundError:
        plt.show()


    plt.clf()


def mostrar():
    plt.show()