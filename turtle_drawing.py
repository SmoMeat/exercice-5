"""turtle_drawing.py : Affiche différente formes avec turtle

Ce fichier permet d'imprimer divers formes animées ou non grace à la bibliothèque
turtle. Pour utiliser les fonctionnalités, vous pouvez importer les fonctions ou
retirer le # devant la fonction désirée dans le runguard.

@Date: 21 mars 2024
@Author: Mathieu Ducharme
@Contact: mathieu.ducharme@umontreal.ca
@Matricule: 20297456
"""

from turtle import *
import time

def carre(taille):
    """Dessine un carré plein

    Args:
        taille (int): taille des cotés
    """
    pensize(taille)
    fd(taille)
    pensize(1)

def triangle(base):
    """Dessine un triangle

    Args:
        base (int): longeur (horizontale) de la base du triangle
    """
    height = base
    precision = 1
    current_base = 0

    for i in range(int(height * precision)):
        slope = base / (2 * height * precision)
        current_base = i * slope

        lt(90); fd(current_base); bk(current_base * 2); fd(current_base)
        rt(90); fd(1 / precision)
    
def ligne(base, taille, n):
    """Dessinne une ligne de petites flèches composés d'un carré et d'un triangle

    Args:
        base (int): longeur (horizontale) de la base du triangle
        taille (int): taille des cotés du carré
        n (int): nombre de flèches
    """
    pu(); bk(100); pd()
    for _ in range(n):
        triangle(base)
        carre(taille)

def spirale(base, taille, nbFormes):
    """Dessine une spirale de flèches fait de carré et de triangle

    Args:
        base (int): longeur (horizontale) de la base du triangle
        taille (int): taille des cotés du carré
        nbFormes (int): nombre de flèches de la plus longue ligne de la spirale
    """
    current_nbFormes = 1

    while current_nbFormes <= nbFormes:
        for _ in range(2):
            pu(); fd(100); pd()
            ligne(base, taille, current_nbFormes)
            
            lt(90)
        current_nbFormes += 1

def spiraleTournante(base, taille, nbFormes, vAng):
    """Dessine une spirale de flèches fait de carré et de triangle
    qui tourne sur elle-meme. 

    Args:
        base (int): longeur (horizontale) de la base du triangle
        taille (int): taille des cotés du carré
        nbFormes (int): nombre de flèches de la plus longue ligne de la spirale
        vAng (int): vitesse angulaire de rotation dans le sens horaire
    """
    angle = 0
    
    while True:
        clear()
        rt(angle)
        spirale(base, taille, nbFormes)
        angle += vAng
        time.sleep(0.01)


if __name__ == '__main__':
    #carre(100)
    #triangle(100)
    #ligne(20, 10, 5)
    #spirale(10, 10, 10)
    #spiraleTournante(15, 10, 10, 2)
    pass