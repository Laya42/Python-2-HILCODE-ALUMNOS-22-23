from Caja_Ahorcado import crear_caja
import Senior_ahorcado
import Letraa

crear_caja(MAX_VERTICAL = 5, MAX_HORIZONTAL = 30, texto = "Hola, ¿preparado para jugar?")
print(Senior_ahorcado.visual[6])
crear_caja(MAX_VERTICAL = 5, MAX_HORIZONTAL = 30, texto = "Hola, ¿preparado para jugar?")
'''
letra = input("¿Qué letra vas a intentar?: ")
while len(letra) != 1:
    letra = input("¿Qué letra vas a intentar?: ")
letra = letra.upper()
'''

letras = ""
letras, Letraa = inputs.input_letras(Letraa)

crear_caja(MAX_VERTICAL = 5, MAX_HORIZONTAL = 30, texto = "Hola, ¿preparado para jugar?")
print(Senior_ahorcado.visual[6])
crear_caja(MAX_VERTICAL = 5, MAX_HORIZONTAL = 30, texto = "Hola, ¿preparado para jugar?")
