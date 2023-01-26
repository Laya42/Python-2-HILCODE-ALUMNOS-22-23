
'''
Semejante al proyecto anterior, vamos a hacer otro proyecto
para adivinar números, sin embargo, nosotros somos los que
decimos que número debe ser adivinado y el ordenador es el
responsáble por adivinarlo en el menor número de turnos posible.
Para ello necesitamos programar el ordenador de tal modo que pueda
convergir al número que indiquiemos nosotros al início del programa.
Hay várias maneras de hacerlo, cabe a vosotros pensar y desarrollar
una manera que el ordenador pueda encontrar el número secreto en el
menor número de turnos posible.
'''

import random



def adivinar(jugador, bot, intentos, MAX):
    while (bot != jugador):
        if bot < jugador:
            print(f"El número {bot} es mayor")
            bot = random.randint(0,MAX)
        if bot > jugador:
            print(f"El número {bot} es menor")
            bot = random.randint(0,MAX)
        intentos = 1

    return intentos, bot



MAX = 100
print("Hola Clovisan bienvenido a tu reto de programación que en realidad es mío asi que espero que tengas el suficiente tiempo libre como Orestes para empezar bueno empecemos...")
jugador = int(input("Elige un número y yo lo voy a intentar adivinar  (no lo veo jaja) : "))
bot = random.randint(0,100)
intentos = 0

intentos, bot = adivinar(jugador, bot, intentos, MAX)

print (f"Acertaste con el número {bot}")

print(f"Ha usado {intentos} intentos. ")





















