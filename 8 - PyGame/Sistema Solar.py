import pygame
import colores

ANCHO = 1080
ALTO = 720
CENTRO = (ANCHO/2, ALTO/2)
NOMBRE = "Sistema Solar"

VENTANA = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption(NOMBRE)

# FUENTE = pygame.font.SysFont("comicsans", 16)

VENTANA.fill(colores.getColor("MARRON"))
pygame.draw.circle(VENTANA, colores.getColor("AMARILLO"), CENTRO, 40)
pygame.draw.circle(VENTANA, colores.getColor("AZUL"), (300, ALTO/2), 15)

pygame.display.update()
