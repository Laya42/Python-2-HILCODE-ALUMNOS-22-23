import pygame
import colores
import math
import Astros

ANCHO = 1080
ALTO = 720
CENTRO = (ANCHO/2, ALTO/2)
NOMBRE = "Sistema Solar"

h = CENTRO[0]
k = CENTRO[1]
angulo_tierra = 0
angulo_marte = 0
angulo_jupiter = 0

VENTANA = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption(NOMBRE)

# r = radio del circulo que queremos dibujar
# h = coordenada x del centro del circulo
# k = coordenada y del centro del circulo
# angulo = punto de inicio del movimiento (siempre vale 0 al empezar)

def movimiento(r, h, k, angulo):
    x = h + int(math.cos(angulo) * r)
    y = k + int(math.sin(angulo) * r)
    return x, y

# FUENTE = pygame.font.SysFont("comicsans", 16)

VENTANA.fill(colores.getColor("NEGRO"))
tierra = Astros.constructorAstros(tam = 15, v_angular = 0.001, color = "AZUL", nombre="Tierra", distancia=300)
sol = Astros.constructorAstros(tam = 40, color = "AMARILLO", nombre="Sol", distancia=0)

# dibujando el sol
pygame.draw.circle(VENTANA, colores.getColor(sol["color"]), CENTRO, sol["tam"])

# moviendo la tierra
tierra["x"], tierra["y"] = movimiento(150, h, k, tierra["angulo"])
tierra["angulo"] = tierra["angulo"] - tierra["v_angular"]
pygame.draw.circle(VENTANA, colores.getColor(tierra["color"]), (tierra["x"],tierra["y"]), tierra["tam"])
pygame.display.update()

'''
ejecuta = True
while ejecuta == True:
    x, y = movimiento(150, h, k, angulo_tierra)
    angulo_tierra = angulo_tierra - vel_angular_tierra
    VENTANA.fill(colores.getColor("NEGRO"))
    pygame.draw.circle(VENTANA, colores.getColor("AMARILLO"), CENTRO, 40)
    pygame.draw.circle(VENTANA, colores.getColor("AZUL"), (x, y), 15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    pygame.display.update()

pygame.quit()
'''
