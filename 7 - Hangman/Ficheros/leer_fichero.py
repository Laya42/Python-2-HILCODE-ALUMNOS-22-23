# Escribe tu código aquí :-)
nombre_fichero = "Todas_Palabras.txt"

# f = open(nombre_fichero,'r')
numeros = []
with open(nombre_fichero,'r') as f:
    for linea in f:
        numeros.append(linea)
        print(linea)

f.close()
print(numeros)



    numeros = []
    with open(nombre_fichero, 'r') as archivo:
        archivo.read()
        print(archivo)
        numeros.append(archivo)
    f.close()



