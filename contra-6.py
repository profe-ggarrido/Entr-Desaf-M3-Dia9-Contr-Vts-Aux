# CONTRA-5.py VARIANTES DE CALCULO TIEMPO
#-----------------------------------------

import random
import datetime
from string import ascii_lowercase
from datetime import timedelta
import time


def probar_contrasena():
    contrasena = input("Ingresa la contraseña (solo letras minúsculas): ")
    intentos = 0

    inicio = datetime.datetime.now()  # Guarda el tiempo de inicio

    while True:
        intentos += 1
        intento = generar_contrasena_aleatoria(len(contrasena))
        print("Intento:", intento)

        if intento == contrasena:
            print("¡Contraseña adivinada!")
            print(inicio)
            
            break

    fin = datetime.datetime.now()  # Guarda el tiempo de término
    print(fin)

    tiempo_total = fin - inicio  # Calcula el tiempo total
    #print(tiempo_total)
    tiempo_formateado = formatear_tiempo(tiempo_total)
    print(type(tiempo_formateado))

    print("Número total de intentos:", intentos)
    print("Tiempo total:", tiempo_formateado)

def generar_contrasena_aleatoria(longitud):
    return ''.join(random.choices(ascii_lowercase, k=longitud))

def formatear_tiempo(tiempo):
    # Obtén la duración total en segundos
    duracion_segundos = tiempo.total_seconds()

    # Calcula las horas, minutos y segundos
    horas = int(duracion_segundos // 3600)
    minutos = int((duracion_segundos % 3600) // 60)
    segundos = int(duracion_segundos % 60)
    milisegundos = int((duracion_segundos - int(duracion_segundos)) * 1000)

    # SE DEVUELVE EL CALCUO FORMTEADO PARA MEJOR VISIBILIDAD
    #HORAS, IN Y SEG CON 2 DIGITOS - MILISEGS. CON 3 DECIM.

    return f"{horas:02}:{minutos:02}:{segundos:02},{milisegundos:03}"
    


#INVESTIGCION/APRENDIZAJE ADICIONAL
#----------------------------------
if __name__ == "__main__":  #CHEQUEO DEL PROGR: Si es el principal o fue importado
    probar_contrasena()
