"""

zenon_dichotomie.py illustre le lancer de pierre de Zénon pour atteindre l'arbre. Selon lui la pierre n'atteindra jamais l'arbre car elle devra
toujours parcourir la moitié de la moitié de la...de la distance entre la position initiale et l'arbre. Pour essayer de coller à une situation réelle
on a utilisé des paraboles pour représenter chaque lancer. La méthode  La procédure est expliquée en détail dans le fichier ReadMe.pdf.

"""
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

t = np.linspace(0, 6, 1000)# construction d'un vecteur abcisse
values = dict() # création  d'un dictionnaire pour stocker les valeurs d'abcisse et d'ordonnée
values["valeurs_positives"] = [] # initialisation du tableau dans lequel sera stocké les valeurs d'ordonnée


# calcul des valeurs de la suite de fonction qui représentera les lancers successifs

for i in range(2,15):    
    values[f"lancer_{i+1}"] = -np.power(t-((np.power(2,i+2)-3)/np.power(2,i)),2) + 1/np.power(2,2*i)  
    # on isole les valeurs positives car ce sont elles qui nous intéresse pour illustrer les lancers
    for item in values[f"lancer_{i+1}"]:    
        if item>0 : values["valeurs_positives"].append(item * (2**(2*i)))
        
# for i in range(len(t)-len(seq["valeurs_positives"])):
        # seq["valeurs_positives"].append(0)

# préparation du graphique matplotlib
fig, ax = plt.subplots()
line = ax.plot(t[0], values["valeurs_positives"][0])[0]
scat = ax.scatter(t[0], values["valeurs_positives"][0])
ax.set(xlim=[0, 1.1], ylim=[0, 1.1], xlabel='Length units', ylabel='Height units')

# les fonctions update sont appelées plus bas par Matplotlib pour tracer le graphique en animation 

def update_rocks(frame):
    
    scat = ax.scatter(t[0], values["valeurs_positives"][0])
    x = t[:frame]
    y = values["valeurs_positives"][:frame]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    return (scat)

def update_line(frame):
    
    #update the line plot:
    line.set_xdata(t[:frame])
    line.set_ydata(values["valeurs_positives"][:frame])
    return(line)
    


# La fonction trace appelle la méthode animation de la classe FuncAnimation pour tracer la courbe en animation.
# On peut choisir 'line' ou 'rocks' en entrée pour avoir deux styles différents de tracés. En effet le style 'rocks' ne permet
# pas d'apprécier correctement les derniers lancers car plus on avance, plus les courbes sont petites et moins il y a de valeurs.
def trace(style):
    
    if style == 'rocks':
        ani = animation.FuncAnimation(fig=fig, func=update_rocks, frames=len(values["valeurs_positives"]), interval=10)
        plt.show()
    elif style == 'line':
        ani = animation.FuncAnimation(fig=fig, func=update_line, frames=len(values["valeurs_positives"]), interval=10)
        plt.show()
    else:
        print("This style isn't recognized. Please enter either 'line' or 'rocks' as input of the function.")


trace_0 = trace('line')
trace_1 = trace('rocks')




