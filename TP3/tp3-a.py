import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo .xlsx
archivo_xlsx = 'TablaCapitales.xlsx'
# Cargar el archivo .xlsx en un DataFrame
df_base = pd.read_excel(archivo_xlsx, index_col=0)
df_base = df_base.iloc[:-2]

def heuristica(ciudad, df):
    if ciudad in df.index:
        # Utiliza 'idxmin' para encontrar la ciudad con la menor distancia a 'ciudad1'
        ciudad_menor_distancia = df.loc[ciudad].idxmin()
        distancia_minima = df.loc[ciudad, ciudad_menor_distancia]
        return ciudad_menor_distancia, distancia_minima
    else:
        print(f"{ciudad} no se encuentra en el DataFrame.")

df_ciudades = df_base
km_recorridos = 0
ciudad_inicial = input("Ingrese ciudad inicial \n")
ciudad_i = ciudad_inicial
cantidad_de_columnas = df_base.shape[1]
recorridos = []

for i in range(1, cantidad_de_columnas):
    
    ciudad_proxima, distancia = heuristica(ciudad_i, df_ciudades)
    df_ciudades = df_ciudades.drop(ciudad_i, axis=1)
    km_recorridos += distancia
    data = [ciudad_i, ciudad_proxima, distancia, km_recorridos]
    recorridos.append(data)
    ciudad_i = ciudad_proxima

km_recorridos += df_base[ciudad_i][ciudad_inicial]
data = [ciudad_i, ciudad_inicial,df_base[ciudad_i][ciudad_inicial], km_recorridos]
recorridos.append(data)

df_recorridos = pd.DataFrame(recorridos, columns=['Ciudad Inicial', 'Ciudad Final', 'Distancia (KM)', 'Total(KM)'])

print(df_recorridos)