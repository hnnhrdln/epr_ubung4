__author__ = "5641727, Redelin, $matrikelnummer, $name"

import random
random.seed(1234)

"""
TODO
Beginn:
-players definieren: ('name des spielers', boolean: über eingabe oder auto)
->vllt in eigener funktion user prompts zur konfigurierung schalten
-user prompt über anzahl der würfel und augenzahl der würfel
-nutzer zu beginn die spielregeln & eingaben erklären. [Return] soll roll_dice ausführen, [n] den "becher" weitergeben

sixteen_is_dead:
-logic umsetzen, aka 10er, 9er, gewinn/verlust koordinieren, spieler anzeigen
->(random risikobereitschaft im pc implementieren? aka pc kann "entscheiden" sein glück zu versuchen und wirft nochmal?)

allgemein:
-error handling -> nicht abbruch bei falscheingabe
-spiel beenden 
-spiel neu starten
"""

def roll_dice(number, faces, seed=None):
    """
    Returns list of thrown dice values. Implements at least one dice.
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
