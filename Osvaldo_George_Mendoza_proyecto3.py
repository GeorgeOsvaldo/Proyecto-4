#importamos las librerias necesarias
#numpy para manejo de arreglos y lo apodaamos np
import numpy as np
# matplotlib para graficar y lo apodamos plt
from matplotlib import pyplot as plt
#random para generar numeros aleatorios y lo apodamos rm
import random as rm

#definimos la simulacion de galton con una funcion
def galton_simulacion(num_bolas=3000, nim_niveles=12):
    #se crea un arreglo de ceros para contar las bolas en cada nivel
    niveles = np.zeros(nim_niveles + 1)
    #se itera sobre el numero de bolas
    for _ in range(num_bolas):
        #se inicia la posicion de la bola en 0
        posicion = 0
        #se itera sobre el numero de niveles
        for _ in range(nim_niveles):
            #se genera un numero aleatorio entre 0 y 1
            if rm.random() < 0.5:
                #si el numero es menor a 0.5, la bola se mueve a la izquierda
                posicion -= 1
            else:
                #si el numero es mayor o igual a 0.5, la bola se mueve a la derecha
                posicion += 1
        #se actualiza el conteo de bolas en el nivel correspondiente
        niveles[(posicion + nim_niveles) // 2] += 1
    #graficamos los resultados
    #plt.bar para crear un grafico de barras 
    #range(nim_niveles + 1) para definir las posiciones en el eje x
    #niveles para definir las alturas de las barras
    #color='red' para definir el color de las barras
    #alpha=0.7 para definir la transparencia de las barras
    plt.bar(range(nim_niveles + 1), niveles, color='red', alpha=0.7)
    #xlabel, ylabel y title para agregar etiquetas y titulo al grafico
    plt.xlabel('Nivel') 
    plt.ylabel('Número de bolas')
    plt.title('Simulación de la Máquina de Galton')
    #plt.show() para mostrar el grafico
    plt.show()
#llamamos a la funcion para ejecutar la simulacion
galton_simulacion()