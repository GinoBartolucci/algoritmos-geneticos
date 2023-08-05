def mochila_exhaustiva(VOL_MOCHILA, objetos):
    mejor_dinero = 0
    mejor_combinacion = []
    
    def buscar_combinaciones(i, volumen_actual, dinero_actual, combinacion_actual):
        nonlocal mejor_dinero, mejor_combinacion

        if i == len(objetos):
            # Si llegamos al final de la lista de objetos, verificamos si esta combinación es mejor
            if dinero_actual > mejor_dinero and volumen_actual <= VOL_MOCHILA:
                mejor_dinero = dinero_actual
                mejor_combinacion = combinacion_actual.copy()
            return

        # No incluir el objeto actual
        buscar_combinaciones(i + 1, volumen_actual, dinero_actual, combinacion_actual)

        # Incluir el objeto actual si no excede el volumen de la mochila
        if volumen_actual + objetos[i][0] <= VOL_MOCHILA:
            buscar_combinaciones(i + 1, volumen_actual + objetos[i][0], dinero_actual + objetos[i][1], combinacion_actual + [objetos[i]])
        


    buscar_combinaciones(0, 0, 0, [])
    return mejor_dinero, mejor_combinacion

VOL_MOCHILA = 4200
objetos = [
    [150, 20],
    [325, 40],
    [600, 50],
    [805, 36],
    [430, 25],
    [1200, 64],
    [770, 54],
    [60, 18],
    [930, 46],
    [353, 28]
]

dinero_en_mochila, combinacion_en_mochila = mochila_exhaustiva(VOL_MOCHILA, objetos)
print("Dinero total en la mochila:", dinero_en_mochila)
print("Combinación de objetos en la mochila:", combinacion_en_mochila)
