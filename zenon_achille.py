"""

Le programme zenon_achille.py comporte deux fonctions. 
La fonction anim_race() simule la course d'Achille contre la tortue grâce à une animation réalisée ave  le module Pygame.
La fonction digit_race() résume la course d'Achille contre la tortue avec un tableau dans lequel sont affichées les positions successives 
des deux protagonistes. Elle affiche ensuite un graphique avec deux courbes affines qui représentent les distances parcourues, avec notamment
le point où Achille dépasse la tortue.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *
import sys


def anim_race(v_achille, v_turtle):
    
    
    size = 1000,1000 #taille de la fenêtre pour l'animation

    pygame.init() # initiation de pygame
    win = pygame.display.set_mode((size)) # on créé la fenêtre qui va acceuillir l'animation
    pygame.display.set_caption("La course d'Achille contre la tortue") # titre de la fenêtre
  
    # coordonnées de départs des participants
    x_achille = 0
    y_achille = 250

    x_turtle = 100
    y_turtle = 300
  
    # Dimension du carré qui va représenter Achille et la tortue
    width = 20
    height = 20

    run = True # On indique que pygame est en route

    # l'animation est une boucle infinie qui affiche un certain nombre d'images par seconde
    while run:

        pygame.time.delay(10) # temps entre les images

        for event in pygame.event.get(): # on doit itérer sur les events Pygame pour qu'il puisse terminer et sortir de la boucle while
 
            if event.type == pygame.QUIT:
                run = False

        win.fill((0, 0, 0)) # application d'une couleur de fond
        
        # actualisation des vitesses respectives
        x_achille += v_achille 
        x_turtle += v_turtle
        
        # on met une condition sur le premier participant à dépasser la ligne, autrement dit à sortir de l'écran
        if x_achille > size[0]:
            print("Achille a gagné contrairement à ce que Zenon affirmait !")
            break
        elif x_turtle > size[0]:
            print("Zenon avait raison !")
            break

        # Achille est représenté par un carré rouge et la tortue par un carré vert
        pygame.draw.rect(win, (255, 0, 0), (x_achille, y_achille, width, height))
        pygame.draw.rect(win, (0, 255, 0), (x_turtle, y_turtle, width, height))
    
        pygame.display.update() # actualisation de la fenêtre

    pygame.quit()

race0 = anim_race(1.2,1)


def digit_race(v_achille, v_turtle, penalty_achille, steps):
    
    if v_turtle > v_achille:
        
        print("Cette histoire n'a plus de sens si la tortue est plus rapide qu'Achille. Entrez une vitesse supérieure pour Achille.")
    else:
        
        race_data = dict()
        position_init_turtle = 0
        position_init_achille = position_init_turtle - np.abs(penalty_achille)
        race_data["positions_achille"] = []
        race_data["positions_turtle"] = []
        
        for i in range(steps+1):
        
            race_data["positions_turtle"].append(position_init_turtle + v_turtle)
            position_init_turtle = race_data["positions_turtle"][i]
        
            race_data["positions_achille"].append(position_init_achille + v_achille)
            position_init_achille = race_data["positions_achille"][i]
            
        race_frame = pd.DataFrame(race_data)
        print(race_frame)
        # traçage des courbes de distance d'Achille et la tortue
        # le point d'intersection des deux courbes est le point où Achille dépasse la tortue
        plt.plot(race_data["positions_turtle"], label = 'Tortue', color = 'g')
        plt.plot(race_data["positions_achille"], label='Achille', color='r')
        plt.title('Courbes normalisées des distances parcourues par Achille et la tortue', fontsize=10)
        plt.xlabel('unités de temps')
        plt.ylabel('unités de longueur')
        plt.legend()
        plt.show()
        
        return race_frame
        
        
        
        
race1 = digit_race(1.5,1,10,30)

