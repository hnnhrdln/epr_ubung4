__author__ = "5641727, Redelin, 6544078, Kervella"

import random
random.seed(1234)

"""
TODO
Beginn:
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

"""
print("Hi, lets play sixteen or dead.\nThe rules: Choose a number or dice and\
throw them until you get as close to 16 as possible.\nBut beware! If you excede 16 you're out. Whoever is closest to 16 wins.\
\nIf your throws add up to 9 you cannot throw again. If they\
add up to 10, you have to throw again.\nEnjoy!")

players = []

while True:
    try:
        number_of_players = int(input("How many players do you want?"))
        break
    except ValueError: 
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
"""

players = [("tick", False),("trick", True),("track", False)]

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

def amount_dice_faces():
    while True:
        try:
            amount_dice = int(input("How many dice do you want?"))
            break
        except ValueError: 
            continue

    while isinstance(amount_dice, int) == False or amount_dice <= 0:
        amount_dice = int(input("How many dice do you want?"))

    while True:
        try:
            amount_faces = int(input("How many faces do your dice have?"))
            break
        except ValueError: 
            continue

    while isinstance(amount_faces, int) == False or amount_faces <= 0:
        amount_faces = int(input("How many faces do your dice have?"))

    return [amount_dice, amount_faces]

def compare_results(score):
    bla = []
    for element in score:
        if element[1] > 16:
            continue
        else:
            bla.append(element)

    best_score = max([player[-1] for player in bla])
    for subarray in bla:
        if best_score in subarray:
            print("The winner is " + subarray[0])



def sixteen_is_dead(players):
    """
    Implementiert ablauf.   
    """
    amount_dice_faces_liste = amount_dice_faces()
    amount_dice = amount_dice_faces_liste[0]
    amount_faces = amount_dice_faces_liste[1]

    score = []
    for element in players:
        score.append([element[0], 0])
    
    for i in range(0,len(players)):
        if players[i][1] == True:

            while True:

                input_human = input("Press ENTER to roll again") #turns out enter ist just empty string input
                if input_human == '' :
                    score_list = roll_dice(amount_dice, amount_faces)
                    print(sum(score_list))
                    score[i][1] = score[i][1] + sum(score_list) 
                    print(score)
                if input_human == 'Nein':
                    players.append(score)
                    break # Züruck zum Anfang
                if score[i][1] == 10:
                    print("Sie müssen jetzt erneut würfeln.")
                    score += roll_dice(amount_dice,6)[i]
                if score[i][1] == 9:
                    print("Sie dürfen nicht mehr würfeln.")
                    players.append(score)
                    break
                if score[i][1] >= 16:
                    print("Sie haben verloren.")
                    break
                    
        else:
            
            while True:

                for _ in range(1, random.randint(1, 5)): #lass den pc jetzt erstmal zufällig oft würfeln
                    score_list = roll_dice(amount_dice, amount_faces)
                    print(sum(score_list))
                    score[i][1] = score[i][1] + sum(score_list) 
                    print(score)
            
                if score[i][1] == 10:
                    print("Sie müssen jetzt erneut würfeln.")
                            
                if score[i][1] == 9:
                    print("Sie dürfen nicht mehr würfeln.")
                    break
                        
                if score[i][1] >= 16:
                    print("Sie haben verloren.")
                    break

    compare_results(score)


sixteen_is_dead(players)

