# Trabajo practico #1
Este trabajo practico consiste en resolver un problema para buscar un máximo de la función mediante algoritmos geneticos. Siendo nuestra función $f(x)$ la siguiente:

$$f(x) = (\frac{x}{2^{30} -1})^2 $$
En el dominio $[0 , 2^{30} -1]$


Teniendo en cuenta los siguientes datos:

* Probabilidad de Crossover = 0,75
* Probabilidad de Mutación = 0,05
* Población Inicial = 10 individuos
* Ciclos del programa = 20
* Método de Selección = Ruleta
* Método de Crossover = 1 Punto
* Método de Mutación = invertida



### Parte A del problema:
* El programa debe mostrar, finalmente, el Cromosoma correspondiente al valor máximo, el valor máximo, mínimo y promedio obtenido de cada población.
* Mostrar la impresión de las tablas de mínimos, promedios y máximos para 20, 100 y 200 corridas.
Deben presentarse las gráficas de los valores Máximos, Mínimos y Promedios de la función objetivo por cada generación luego de correr el algoritmo genético 20, 100 y 200 iteraciones (una gráfica por cada conjunto de iteraciones)
* Realizar comparaciones de las salidas corriendo el mismo programa en distintos ciclos de corridas y además realizar todos los cambios que considere oportunos en los parámetros de entrada de manera de enriquecer sus conclusiones.

### Parte B del problema: 
* Se realiza un muestreo en una élite de “ere” miembros es decir para nuestro ejercicio se seleccionan dos cromosomas que posean el mejor fitness de entre los mejores de la población inicial y se incorporan directamente a la población siguiente, sin pasar por la población intermedia.

* El proceso se repite para cada población que se va generando hasta completar el número de veces que se ejecutará el algoritmo genético. Se solicita la ejecución de 100 iteraciones.

    Para esta segunda parte del trabajo se deberá utilizar elitismo, mostrar nuevamente las salidas por pantalla y las gráficas solicitadas en la PARTE A pero en este caso considerando la aplicación de elitismo. 

    Resolver el ejercicio realizando 100 iteraciones del algoritmo.

