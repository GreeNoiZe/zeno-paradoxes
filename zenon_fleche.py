"""

Le programme zenon_fleche.py simule la trajectoire d'une flèche vers une cible. On n'a choisi une trajectoire linéaire et on a préféré s'attarder sur le caractère 
discret de la trajectoire pour apprécier les positions successives de la flèche. 

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *
import sys


# couleurs qui vont nous servir pour l'animation
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

size = 1000,1000 #taille de la fenêtre pour l'animation
y0 = size[0]/3 # repère pour dessiner les objets
x_fleche = 0 # position initiale de la flèche

pygame.init() # initiation de pygame
win = pygame.display.set_mode((size)) # on créé la fenêtre qui va acceuillir l'animation
pygame.display.set_caption("La flèche vole vers sa cible, mais l'atteindra-t-elle ?") # titre de la fenêtre

run = True # On indique que pygame est en route

# l'animation est une boucle infinie qui affiche un certain nombre d'images par seconde
while run:

    pygame.time.delay(500) # temps entre les images

    for event in pygame.event.get(): # on doit itérer sur les events Pygame pour qu'il puisse terminer et sortir de la boucle while
 
        if event.type == pygame.QUIT:
            run = False

    win.fill((170,170,170)) # application d'une couleur de fond
        
        
    x_fleche += 40
    # on met une condition sur le premier participant à dépasser la ligne, autrement dit à sortir de l'écran
    if x_fleche == size[0] - 40:
        print("La flèche a atteind la cible contrairement à ce que Zenon affirmait !")
        break
    # On dessine des ellipses les unes sur les autres pour représenter une cible vue de côté 
    pygame.draw.ellipse(win, WHITE, (size[0]-100,y0-100,100,200))
    pygame.draw.ellipse(win, BLACK, (size[0]-90,y0-80,80,160))
    pygame.draw.ellipse(win, BLUE, (size[0]-80,y0-60,60,120))
    pygame.draw.ellipse(win, RED, (size[0]-70,y0-40,40,80))
    pygame.draw.ellipse(win, YELLOW, (size[0]-60,y0-20,20,40))
    # On dessinne la flèche grâce à la méthode polygone de Pygame
    pygame.draw.polygon(win, (115,0,0), ((x_fleche, y0 - 2), (x_fleche, y0 + 2), (x_fleche + 30, y0 + 2), (x_fleche + 30, y0 + 7), (x_fleche + 40, y0), (x_fleche + 30, y0 - 7), (x_fleche + 30, y0 - 2)))
    
    pygame.display.update() # actualisation de la fenêtre

pygame.quit()

