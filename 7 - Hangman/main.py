import horca
from caja import crear_caja
import palabras
import inputs
import checks

palabra = palabras.palabra
guiones = "_" * len(palabra)
letras = ""
vidas = 6
crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = "¡Hola, Bienvenido al juego!")
print(horca.visual[vidas])
crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = guiones)

while vidas != 0 and guiones != palabra:
    letras, letra = inputs.input_letras(letras)
    guiones, vidas = checks.checks(palabra, guiones, letra, vidas)

    if guiones == palabra:
        texto = "¡Enhorabuenas! La palabra era " + palabra
    elif vidas == 0:
        texto = "GAME OVER"
    else:
        texto = letras

    crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = texto)
    print(horca.visual[vidas])
    crear_caja(MAX_HORIZONTAL = 40, MAX_VERTICAL = 5, texto = guiones)

    if vidas == 0:
        print("La palabra era",palabra)

