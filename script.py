__author__ = "5641727, Redelin, $matrikelnummer, $name"

import random

def roll_dice(number, faces, seed=None):
    liste = []                  #keine Ahnung ob das eine gute Idee ist die Liste so zu definieren
    for i in range (0,number):
        liste.append(random.randrange(1,faces+1))
    print(liste)