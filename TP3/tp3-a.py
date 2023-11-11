# instalar Pillow (pip install Pillow)
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# Ruta al archivo .xlsx
archivo_xlsx = 'TablaCapitales.xlsx'
# Cargar el archivo .xlsx en un DataFrame
df_base = pd.read_excel(archivo_xlsx, index_col=0)
df_base = df_base.iloc[:-2]

def dibujar_linea(imagen, punto_inicio, punto_fin, color, grosor=1):
    draw = ImageDraw.Draw(imagen)
    draw.line([punto_inicio, punto_fin], fill=color, width=grosor)

def heuristica(ciudad, df):
    if ciudad in df.index:
        # Utiliza 'idxmin' para encontrar la ciudad con la menor distancia a 'ciudad1'
        ciudad_menor_distancia = df.loc[ciudad].idxmin()
        distancia_minima = df.loc[ciudad, ciudad_menor_distancia]
        return ciudad_menor_distancia, distancia_minima
    else:
        print(f"{ciudad} no se encuentra en el DataFrame.")

imagen = Image.open("mapa.png")
df_ciudades = df_base
km_recorridos = 0
ciudad_inicial = input("Ingrese ciudad inicial \n")
ciudad_i = ciudad_inicial
cantidad_de_columnas = df_base.shape[1]
recorridos = []
coordenadas = { "Santa Fe": (186,168), "Paraná": (214,181), "Córdoba": (146,185), "San Luis": (113,210), "Mendoza": (74,201), "San Juan": (77,178), "La Rioja": (102,145), "S.F.d.V.d. Catamarca": (115,122), "Sgo. Del Estero": (140,113), "S.M. de Tucumán": (124,99), "Salta": (122,61), "S.S. de Jujuy": (124,52),"Resistencia": (217,102), "Corrientes": (225,107), "Formosa": (234,85), "Posadas": (269,110), "Cdad. de Bs. As.": (229,238), "La Plata": (218,226), "Santa Rosa": (139,264), "Neuquén": (86,303), "Viedma": (158,334), "Rawson": (129,374), "Río Gallegos": (91,519), "Ushuaia": (108,568) }

for i in range(1, cantidad_de_columnas):
    
    ciudad_proxima, distancia = heuristica(ciudad_i, df_ciudades)
    df_ciudades = df_ciudades.drop(ciudad_i, axis=1)
    km_recorridos += distancia
    data = [ciudad_i, ciudad_proxima, distancia, km_recorridos]
    recorridos.append(data)
    dibujar_linea(imagen, coordenadas[ciudad_i], coordenadas[ciudad_proxima], color="red", grosor=1)
    ciudad_i = ciudad_proxima

km_recorridos += df_base[ciudad_i][ciudad_inicial]
data = [ciudad_i, ciudad_inicial,df_base[ciudad_i][ciudad_inicial], km_recorridos]
recorridos.append(data)
dibujar_linea(imagen, coordenadas[ciudad_i], coordenadas[ciudad_inicial], color="red", grosor=1)

df_recorridos = pd.DataFrame(recorridos, columns=['Ciudad Inicial', 'Ciudad Final', 'Distancia (KM)', 'Total(KM)'])

imagen.save("imagen_con_lineas.png")
imagen.show()
print(df_recorridos)