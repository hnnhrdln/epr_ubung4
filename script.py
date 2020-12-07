__author__ = "5641727, Redelin, $matrikelnummer, $name"

import random

random.seed(1234)

def roll_dice(number, faces, seed=None):
    """
    Returns list of thrown dice values. Implements at least one throw.
    """
    if number < 1:
        number = 1

    dice_throws = []                  #keine Ahnung ob das eine gute Idee ist die Liste so zu definieren
    for i in range (0,number):
        dice_throws.append(random.randrange(1,faces+1))
    return dice_throws


def sixteen_is_dead( players):
    """
    implementiert ablauf. 
    players ist eine liste aus tupel
    """
    print(roll_dice(6,6, None))

sixteen_is_dead("bla")
