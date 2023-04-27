def leer_fichero(nombre_fichero):
    lista_palabra = []
    with open(nombre_fichero, "r") as f:
        for palabra in f:
                palabra = palabra.replace("\n", "")
                lista_palabra.append(palabra)

        f.close()
    return lista_palabra
