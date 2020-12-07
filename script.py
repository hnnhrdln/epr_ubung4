__author__ = "5641727, Redelin, $Matrikelnummer, $Nachname"
import random

def roll_dice(number, faces, seed=None):
    liste = []
    for i in range (0,number):
        liste.append(random.randrange(1,faces+1))
    print(liste)
