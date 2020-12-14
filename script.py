"""16 is dead."""
__author__ = "5641727, Redelin, 6544078, Kervella"

import random
import time
random.seed(1234)

#Game set-up

print("Hi, lets play sixteen or dead.\nThe rules: Choose a number or dice and\
throw them until you get as close to 16 as possible.\nBut beware! If you excede 16 you're out. Whoever is closest to 16 wins.\
\nIf your throws add up to 9 you cannot throw again. If they\
add up to 10, you have to throw again.\nEnjoy!")

players = []

while True:
    try:
        number_of_players = int(input("How many players do you want to play with?"))
        break
    except ValueError: 
        continue

while isinstance(number_of_players, int) == False or number_of_players <= 0:
    number_of_players = int(input("How many players do you want to play with?"))

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


players = [("tick", True),("trick", True),("track", False)]

#some loop to fill lst


def roll_dice(number, faces, seed=None):
    """
    Function used to define the results obtained from the dice throws in form of a list
    """
    if number < 1:
        number = 1

    dice_throws = []                  #keine Ahnung ob das eine gute Idee ist die Liste so zu definieren
    for i in range (0,number):
        dice_throws.append(random.randrange(1,faces+1))
    return dice_throws


def amount_dice_faces():
    """
    Function used to define the amount of faces the dice, or dices, we use to play, have.
    """
    while True:
        try:
            amount_dice = int(input("How many dices do you want to use?"))
            break
        except ValueError: 
            continue

    while isinstance(amount_dice, int) == False or amount_dice <= 0:
        amount_dice = int(input("How many dices do you want to use?"))

    while True:
        try:
            amount_faces = int(input("How many faces does your dice have?"))
            break
        except ValueError: 
            continue

    while isinstance(amount_faces, int) == False or amount_faces <= 0:
        amount_faces = int(input("How many faces does your dice have?"))

    return [amount_dice, amount_faces]


def compare_results(score):
    """
    Quick comparaison of multiple results from all the players to return a winner
    """
    non_disqualified = [] #wir benötigen einen besseren Namen
    for element in score:
        if element[1] > 16:
            continue
        else:
            non_disqualified.append(element)

    for player in score:
        print(player[0] + " has " + str(player[1]) + " points")

    best_score = max([player[-1] for player in non_disqualified])
    for subarray in non_disqualified:
        if best_score in subarray:
            print("\nThe winner is " + subarray[0])
            print("_____________________________________________")




def sixteen_is_dead(players):
    """
    Main function used to play the game with all the given variables and all the functions defined before
    """
    amount_dice_faces_liste = amount_dice_faces()
    amount_dice = amount_dice_faces_liste[0]
    amount_faces = amount_dice_faces_liste[1]

    score = []
    for element in players:
        score.append([element[0], 0])
    
    for i in range(0,len(players)):
        if players[i][1] == True:
            print("\nYour turn!")

            while True:

                input_human = input("Press ENTER to roll again or next[n]") #turns out enter ist just empty string input
                if input_human == '' :
                    score_list = roll_dice(amount_dice, amount_faces)
                    print(sum(score_list))
                    score[i][1] = score[i][1] + sum(score_list) 
                    print(score)
                if input_human == 'No':
                    players.append(score)
                    break # Züruck zum Anfang
                if score[i][1] == 10:    # 3 Sekunden automatisch warten sprich keine erneute Eingabe
                    print("You have to roll again.")
                    score += roll_dice(amount_dice,6)[i]
                    time.sleep(3)
                if score[i][1] == 9:
                    print("You can't roll again.")
                    players.append(score)
                    break
                if score[i][1] >= 16:
                    print("You have lost.")
                    break
                if input_human == 'n':
                    break
                    
        else:
            print("\nNow its the computers turn. Woohoo")
            
            for _ in range(1, random.randint(1, 5)): #lass den pc jetzt erstmal zufällig oft würfeln
                score_list = roll_dice(amount_dice, amount_faces)
                score[i][1] = score[i][1] + sum(score_list) 
        
                if score[i][1] == 10:
                    print("Sie müssen jetzt erneut würfeln.") #Soll überhaupt ein Text kommen wenn der Computer spielt ?
                    #time.sleep(3)
                    score_list = roll_dice(amount_dice, amount_faces)
                    score[i][1] = score[i][1] + sum(score_list) 

                if score[i][1] == 9:
                    print("Sie dürfen nicht mehr würfeln.")
                    break
                        
                if score[i][1] >= 16:
                    print("Sie haben verloren.")
                    break
                

    compare_results(score)

while True:
    sixteen_is_dead(players)
    prompt = input("Do you want to play another round?[y/n]")
    if prompt == "y":
        sixteen_is_dead(players)
    if prompt == "n":
        print("Cool, been real, bye")
        break

