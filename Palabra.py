from nombre_fichero import leer_fichero
import random

def escoge_palabra(palabras):
    elegir_palabra = random.randint(0, len(palabras)-1)
    palabra = palabras[elegir_palabra]
    return palabra

nombre_fichero = "fichero_palabras.txt"
palabras = leer_fichero(nombre_fichero)
palabra = escoge_palabra(palabras)
print(palabra)
