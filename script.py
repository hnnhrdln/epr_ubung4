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
#Game set-up

print("Hi, lets play sixteen or dead.\nThe rules: Choose a number or dice and\
throw them until you get as close to 16 as possible.\nBut beware! If you excede 16 you're out. Whoever is closest to 16 wins.\
\nIf your throws add up to 9 you cannot throw again. If they\
add up to 10, you have to throw again.\nEnjoy!")

players = []

while True:
    try:
        number_of_players = int(input("How many players do you want?"))
        break
    except: 
        continue

while isinstance(number_of_players, int) == False or number_of_players <= 0:
    number_of_players = int(input("How many players do you want?"))

for x in range(0, number_of_players):
    name = input("What is the name of player "+str(x+1)+"?\n")
    player_or_pc = input("Who is the player played by? [me/pc]\n")
    while player_or_pc != "me" and player_or_pc != "pc":
        player_or_pc = input("Try again! Who is the player played by? [me/pc]\n")
    
    if player_or_pc == "me":
        player_or_pc = True
    elif player_or_pc == "pc":
        player_or_pc = False

    player_tuple = (name, player_or_pc)

    players.append(player_tuple)

print(players)



#some loop to fill lst


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


def sixteen_is_dead(players):
    """
    implementiert ablauf. 
    players ist eine liste aus tupel
    """
    print(roll_dice(6,6, None))


sixteen_is_dead(players)
