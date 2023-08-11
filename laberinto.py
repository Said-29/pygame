import pygame
import sys
import os
from pygame.locals import *
import pyautogui

pygame.init
DISPLAYSURF = pygame.display.set_mode((500,500))
pygame.display.set_caption("Laberinto")

maze = pygame.image.load('laberinto.png')

coord_x = 30
coord_y = 165

player_color = (255,0,0)

map_color = (255,255,255,255)

pygame.key.set_repeat(50,20)

while True:
    
    for event in pygame.event.get():
        DISPLAYSURF.fill((255,255,255))
        DISPLAYSURF.blit(maze,(0,0))

        player = pygame.draw.rect(DISPLAYSURF, player_color, (coord_x,coord_y,5,5))
        finish = pygame.draw.rect(DISPLAYSURF, map_color, (300,40,40,10))

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:

            pressed = pygame.key.get_pressed()
            
            if event.key == pygame.K_LEFT:
                border_color = DISPLAYSURF.get_at((coord_x-5,coord_y))
                low_border_color = DISPLAYSURF.get_at((coord_x-5,coord_y+5))
                if border_color == map_color and low_border_color == map_color:
                    coord_x -= 5

            if event.key == pygame.K_RIGHT:
                border_color = DISPLAYSURF.get_at((coord_x+5,coord_y))
                low_border_color = DISPLAYSURF.get_at((coord_x+5,coord_y+5))
                if border_color == map_color and low_border_color == map_color:
                    coord_x += 5

            if event.key == pygame.K_UP:
                border_color = DISPLAYSURF.get_at((coord_x,coord_y-5))
                low_border_color = DISPLAYSURF.get_at((coord_x+5,coord_y-5))
                if border_color == map_color and low_border_color == map_color:
                    coord_y -= 5
                    
            if event.key == pygame.K_DOWN:
                border_color = DISPLAYSURF.get_at((coord_x,coord_y+5))
                low_border_color = DISPLAYSURF.get_at((coord_x+5,coord_y+5))
                if border_color == map_color and low_border_color == map_color:
                    coord_y += 5

        collide = player.colliderect(finish)

        if collide:
            pygame.display.set_caption("Has ganado")
            ans = pyautogui.confirm(title="Felicidades",text="Has ganado!", buttons=['Volver a jugar','Cerrar'])
            if ans == 'Cerrar':
                pygame.quit()
                sys.exit()
            else:
                pygame.display.set_caption("Laberinto")
                coord_x = 30
                coord_y = 165

    pygame.display.update()