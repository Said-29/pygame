import pygame
import sys
import os
from pygame.locals import *

pygame.init
DISPLAYSURF = pygame.display.set_mode((600,600))
pygame.display.set_caption("Actividad 1")

colorCuadro01 = (255,255,0)
colorCuadro02 = (0,255,255)
coordx1 = 150
coordy1 = 150

while True:
    
    for event in pygame.event.get():
        DISPLAYSURF.fill((0,0,0))
        cuadro01 = pygame.draw.rect(DISPLAYSURF, colorCuadro01, (coordx1,coordy1,300,300))
        cuadro02 = pygame.draw.rect(DISPLAYSURF, colorCuadro02, (200,200,200,200))

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.display.set_caption("IZQUIERDA")
                coordx1 -= 5
            if event.key == pygame.K_RIGHT:
                pygame.display.set_caption("DERECHA")
                coordx1 += 5
            if event.key == pygame.K_UP:
                pygame.display.set_caption("ARRIBA")
                coordy1 -= 5
            if event.key == pygame.K_DOWN:
                pygame.display.set_caption("ABAJO")
                coordy1 += 5

    pygame.display.update()